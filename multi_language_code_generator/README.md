# Security Exposure Path Finder

A small, deterministic graph-search project inspired by the proposed **FAULT//INE** cybersecurity application and its vision of visualising relationships between systems and potential exposure paths.

## What this project does

Given a **predefined directed graph** of systems and connections, the program uses **Breadth-First Search (BFS)** to find a path with the fewest hops from a start node to a target node. It explores neighbouring nodes in ascending ASCII order so equal-length paths produce the same answer across languages.

**BFS Explained:** start at one system, examine its immediate neighbours, then their neighbours, level by level. A queue keeps track of which system to explore next. A visited set prevents loops. When the target is found, parent links reconstruct the path.

This is **connectivity analysis**, not proof of an exploitable attack chain. A connection alone does not establish vulnerability, access permissions or exploitability.

## Input and output

Supply one JSON document as a file:

```json
{
  "nodes": ["WEB", "APP", "AUTH", "DB"],
  "edges": [["WEB", "AUTH"], ["WEB", "APP"], ["AUTH", "DB"], ["APP", "DB"]],
  "start": "WEB",
  "target": "DB"
}
```

Expected output:

```json
{"path": ["WEB", "APP", "DB"], "hops": 2}
```

If no path exists, the program returns `{"path": [], "hops": null}`. Invalid requests return a structured `error` object. See [cross_language_spec.md](cross_language_spec.md) for the exact contract.

## Run the Python reference

Requires Python 3.9+ and no third-party packages. From this project directory:

```bash
python reference/logical_path_finder.py reference/sample_network.json
python -m unittest discover -s reference/tests -v
```

The command reads the supplied JSON file and prints one JSON response to standard output. Invalid input also produces JSON and exits with status 1.

## FAULT//INE - Project Inspiration

FAULT//INE is a **proposed** security-analysis application intended to help developers and security professionals understand weaknesses, system relationships and potential attack chains. This coursework explores one reusable building block of that broader concept, not a complete FAULT//INE feature.

In a future authorised environment, a **separate discovery component** might identify systems and collect evidence of their connectivity through approved inventories, configuration data, APIs or scoped network observations. 

A **graph-building component** would verify and transform those relationships into directed nodes and edges. The BFS component could then identify possible connection paths, and FAULT//INE's interface could visualise them for further investigation.

**Potential future flow:** authorised discovery → verified graph construction → BFS path analysis → FAULT//INE visualisation.

Discovery, scanning, vulnerability assessment, exploit validation and user-interface development are **out of scope** here. Keeping these responsibilities separate makes the BFS algorithm reproducible, testable and straightforward to translate.

## Cross-language plan

1. **Task 0:** Specify the algorithm, JSON contract, edge cases and test vectors in `cross_language_spec.md`.
2. **Task 1:** Build and test the Python reference implementation in `reference/`.
3. **Later tasks:** Translate to JavaScript and Go, run identical vectors and benchmark comparable in-memory BFS workloads.

For fair benchmarks, separate JSON parsing/file I/O from BFS timing, use the same generated graphs and report environment and dataset sizes.
