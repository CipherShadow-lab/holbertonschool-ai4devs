"""Deterministic directed-graph BFS path finder. Standard library only."""

import json
import re
import sys
from collections import deque
from pathlib import Path

NAME = re.compile(r"^[A-Za-z0-9_]+$", re.ASCII)
FIELDS = ("nodes", "edges", "start", "target")


class InputError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(message)


def fail(code, message):
    raise InputError(code, message)


def valid_name(value):
    return isinstance(value, str) and bool(NAME.fullmatch(value))


def check_name(value):
    if not valid_name(value):
        fail("INVALID_NODE_NAME", "Node names must contain only ASCII letters, digits and underscores.")


def find_path(data):
    """Validate a parsed JSON value and return the BFS response or raise InputError."""
    if not isinstance(data, dict):
        fail("INVALID_INPUT", "Input must be a JSON object.")
    for field in FIELDS:
        if field not in data:
            fail("MISSING_FIELD", f"Missing required field: {field}.")
    if any(field not in FIELDS for field in data):
        fail("INVALID_INPUT", "Unexpected top-level field.")

    nodes = data["nodes"]
    if not isinstance(nodes, list) or not nodes:
        fail("INVALID_NODES", "Nodes must be a non-empty array.")
    known = set()
    for node in nodes:
        check_name(node)
        if node in known:
            fail("DUPLICATE_NODE", "Node names must be unique.")
        known.add(node)

    edges = data["edges"]
    if not isinstance(edges, list):
        fail("INVALID_EDGES", "Edges must be an array.")
    adjacency = {node: set() for node in nodes}
    for edge in edges:
        if not isinstance(edge, list) or len(edge) != 2:
            fail("INVALID_EDGE", "Each edge must contain exactly two node names.")
        source, dest = edge
        check_name(source)
        check_name(dest)
        if source not in known or dest not in known:
            fail("UNKNOWN_EDGE_NODE", "Edge references an unknown node.")
        adjacency[source].add(dest)

    for field in ("start", "target"):
        check_name(data[field])
        if data[field] not in known:
            fail("UNKNOWN_NODE", "Start or target node does not exist.")

    start, target = data["start"], data["target"]
    if start == target:
        return {"path": [start], "hops": 0}

    queue = deque([start])
    parents = {start: None}
    while queue:
        node = queue.popleft()
        for neighbour in sorted(adjacency[node]):
            if neighbour in parents:
                continue
            parents[neighbour] = node
            if neighbour == target:
                path = [target]
                while parents[path[-1]] is not None:
                    path.append(parents[path[-1]])
                path.reverse()
                return {"path": path, "hops": len(path) - 1}
            queue.append(neighbour)
    return {"path": [], "hops": None}


def process_text(text):
    """Process raw JSON, always returning a JSON-serialisable response."""
    try:
        data = json.loads(text)
    except (ValueError, TypeError):
        return {"error": {"code": "INVALID_JSON", "message": "Input is not valid JSON."}}
    try:
        return find_path(data)
    except InputError as exc:
        return {"error": {"code": exc.code, "message": exc.message}}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print("Usage: python logical_path_finder.py INPUT.json", file=sys.stderr)
        return 2
    try:
        content = Path(argv[0]).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"Cannot read input file: {exc}", file=sys.stderr)
        return 2
    result = process_text(content)
    print(json.dumps(result, separators=(",", ":")))
    return 1 if "error" in result else 0


if __name__ == "__main__":
    sys.exit(main())
