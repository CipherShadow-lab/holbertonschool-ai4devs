# Cross-Language Specification: Security Exposure Path Finder

## Purpose

Implement deterministic **Breadth-First Search (BFS)** on a **directed, unweighted graph** to find a path with the fewest edges (hops) between a designated start and target. This is a graph-connectivity demonstration, not vulnerability scanning or exploit validation.

## Input Contract

Input is one UTF-8 JSON object with **exactly** these four required keys (additional keys are invalid):

- `nodes`: non-empty array of **unique** node identifiers.
- `edges`: array of directed edges, each exactly `[source, destination]`.
- `start`: node identifier present in `nodes`.
- `target`: node identifier present in `nodes`.

Each identifier is a non-empty JSON string matching `^[A-Za-z0-9_]+$`. Names are **case-sensitive**. Every edge endpoint must appear in `nodes`. Self-loops are valid. Duplicate edges are ignored. Input order does not affect the result. There is no network discovery or automatic scanning.

## Algorithm

1. Validate the input in the order defined below.
2. Build an adjacency list from `nodes` and `edges`, ignoring duplicate edges.
3. Sort each node's outgoing neighbours in **ascending ASCII code-point order** (case-sensitive; e.g. `A` before `B` before `a`).
4. Run BFS from `start` using a FIFO queue and a visited set. Record each newly discovered node's parent exactly once.
5. On reaching `target`, reconstruct the route using parent links. Because BFS explores layers in order, the returned path has the fewest hops. Ordered neighbours choose the lexicographically smallest node sequence among shortest paths.
6. If `target` is not reachable, return an empty path.

`start == target` produces a one-node path and zero hops. Expected time complexity after adjacency preparation: `O(V + E)` for BFS; sorting neighbours adds ordering overhead. Expected memory: `O(V + E)` including adjacency storage.

## Output Contract

Success: `{"path": ["A", "B"], "hops": 1}`. `path` contains identifiers in traversal order, including both endpoints. `hops` is `len(path) - 1`.

Unreachable target: `{"path": [], "hops": null}`.

Invalid input: `{"error": {"code": "ERROR_CODE", "message": "Exact message."}}`. Errors have no `path` or `hops` fields. For the CLI, print the response as JSON and exit 1 for errors (0 for valid searches).

## Validation and Error Precedence

Return the **first** applicable error in this sequence:

1. Unparseable JSON → `INVALID_JSON`: `Input is not valid JSON.`

2. Top-level value not a JSON object → `INVALID_INPUT`: `Input must be a JSON object.`  

3. Missing required keys, checked in order `nodes`, `edges`, `start`, `target` → `MISSING_FIELD`: `Missing required field: <key>.`  

4. Any extra top-level key → `INVALID_INPUT`: `Unexpected top-level field.`  

5. `nodes` not an array or empty → `INVALID_NODES`: `Nodes must be a non-empty array.`  

6. Each node in array order: invalid identifier → `INVALID_NODE_NAME`: `Node names must contain only ASCII letters, digits and underscores.`; repeated identifier → `DUPLICATE_NODE`: `Node names must be unique.`  

7. `edges` not an array → `INVALID_EDGES`: `Edges must be an array.`  

8. Each edge in array order: not a two-item array → `INVALID_EDGE`: `Each edge must contain exactly two node names.`; invalid endpoint identifier → `INVALID_NODE_NAME` (same message as above); unknown endpoint → `UNKNOWN_EDGE_NODE`: `Edge references an unknown node.`  
9. `start`, then `target`: invalid identifier → `INVALID_NODE_NAME` (same message); identifier absent from nodes → `UNKNOWN_NODE`: `Start or target node does not exist.`  

No implicit type conversion or case normalisation. JSON booleans and numbers are not valid identifiers. Error messages and codes are fixed for cross-language equivalence.  

## Edge Cases

- No route and disconnected nodes return `path: []` and `hops: null`.
- Start equal to target returns `[start]` and `0`.
- Directed edges are not automatically reversible.
- Cycles and self-loops terminate because each node is visited at most once.
- Duplicate edges are ignored; unordered input edges still yield the same path.
- Empty graphs, unknown nodes, malformed input and invalid edge shapes return structured errors.

## Test Vectors (12 Required Scenarios)

Each vector below uses the exact input/output contract; `E` abbreviates `edges` and `N` abbreviates `nodes` **only in this table**, not in actual JSON.

| # | Scenario | N | E | start → target | Expected output |
|---|---|---|---|---|---|
| 1 | Direct edge | A,B | A→B | A→B | `path=[A,B]; hops=1` |
| 2 | Multi-hop | A,B,C | A→B, B→C | A→C | `path=[A,B,C]; hops=2` |
| 3 | Equal-length tie | A,B,C,D | A→C, A→B, C→D, B→D | A→D | `path=[A,B,D]; hops=2` |
| 4 | No route | A,B | (none) | A→B | `path=[]; hops=null` |
| 5 | Same node | A | (none) | A→A | `path=[A]; hops=0` |
| 6 | Direction matters | A,B | A→B | B→A | `path=[]; hops=null` |
| 7 | Cycle | A,B,C,D | A→B, B→C, C→A, C→D | A→D | `path=[A,B,C,D]; hops=3` |
| 8 | Duplicate edge | A,B | A→B, A→B | A→B | `path=[A,B]; hops=1` |
| 9 | Edge order | A,B,C,D | C→D, A→C, B→D, A→B | A→D | `path=[A,B,D]; hops=2` |
| 10 | Disconnected node | A,B,C | A→B | A→C | `path=[]; hops=null` |
| 11 | Unknown target | A | (none) | A→Z | `UNKNOWN_NODE` error |
| 12 | Empty graph | (none) | (none) | A→B | `INVALID_NODES` error |

<br>
For vectors 11 and 12, the complete expected error objects are respectively `{"error":{"code":"UNKNOWN_NODE","message":"Start or target node does not exist."}}` and `{"error":{"code":"INVALID_NODES","message":"Nodes must be a non-empty array."}}`.

## Implementation and Equivalence

Python is the reference language; JavaScript and Go translations must produce semantically identical JSON values for the same input, including exact paths, hop counts and error codes/messages. JSON object key order and insignificant whitespace are not significant. All implementations must apply the same validation precedence and ASCII ordering.

## Scope Exclusions

No active network scanning, data collection, vulnerability verification, exploit simulation, risk scoring, persistent storage or UI. Any future FAULT//INE integration would require a separate authorised discovery and graph-building stage.
