"""Automated reference tests for the cross-language specification."""
import importlib.util
import json
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("logical_path_finder", Path(__file__).resolve().parents[1] / "logical_path_finder.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def query(nodes, edges, start, target):
    return module.find_path({"nodes": nodes, "edges": edges, "start": start, "target": target})


class TestPathFinder(unittest.TestCase):
    def test_01_direct(self):
        self.assertEqual(query(["A", "B"], [["A", "B"]], "A", "B"), {"path": ["A", "B"], "hops": 1})

    def test_02_multihop(self):
        self.assertEqual(query(["A", "B", "C"], [["A", "B"], ["B", "C"]], "A", "C"), {"path": ["A", "B", "C"], "hops": 2})

    def test_03_tie(self):
        self.assertEqual(query(["A", "B", "C", "D"], [["A", "C"], ["A", "B"], ["C", "D"], ["B", "D"]], "A", "D"), {"path": ["A", "B", "D"], "hops": 2})

    def test_04_no_path(self):
        self.assertEqual(query(["A", "B"], [], "A", "B"), {"path": [], "hops": None})

    def test_05_same_node(self):
        self.assertEqual(query(["A"], [], "A", "A"), {"path": ["A"], "hops": 0})

    def test_06_directed(self):
        self.assertEqual(query(["A", "B"], [["A", "B"]], "B", "A"), {"path": [], "hops": None})

    def test_07_cycle(self):
        self.assertEqual(query(["A", "B", "C", "D"], [["A", "B"], ["B", "C"], ["C", "A"], ["C", "D"]], "A", "D"), {"path": ["A", "B", "C", "D"], "hops": 3})

    def test_08_duplicates(self):
        self.assertEqual(query(["A", "B"], [["A", "B"], ["A", "B"]], "A", "B"), {"path": ["A", "B"], "hops": 1})

    def test_09_unsorted_edges(self):
        self.assertEqual(query(["A", "B", "C", "D"], [["C", "D"], ["A", "C"], ["B", "D"], ["A", "B"]], "A", "D"), {"path": ["A", "B", "D"], "hops": 2})

    def test_10_disconnected(self):
        self.assertEqual(query(["A", "B", "C"], [["A", "B"]], "A", "C"), {"path": [], "hops": None})

    def test_11_unknown_node(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A"], "edges": [], "start": "A", "target": "Z"})), {"error": {"code": "UNKNOWN_NODE", "message": "Start or target node does not exist."}})

    def test_12_empty_graph(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": [], "edges": [], "start": "A", "target": "B"})), {"error": {"code": "INVALID_NODES", "message": "Nodes must be a non-empty array."}})

    def test_13_invalid_json(self):
        self.assertEqual(module.process_text("{" )["error"]["code"], "INVALID_JSON")

    def test_14_invalid_edge_shape(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A"], "edges": [["A"]], "start": "A", "target": "A"}))["error"]["code"], "INVALID_EDGE")

    def test_15_invalid_name(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A-B"], "edges": [], "start": "A-B", "target": "A-B"}))["error"]["code"], "INVALID_NODE_NAME")

    def test_16_duplicate_nodes(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A", "A"], "edges": [], "start": "A", "target": "A"}))["error"]["code"], "DUPLICATE_NODE")

    def test_17_self_loop(self):
        self.assertEqual(query(["A", "B"], [["A", "A"], ["A", "B"]], "A", "B"), {"path": ["A", "B"], "hops": 1})

    def test_18_case_sensitive_ascii_order(self):
        self.assertEqual(query(["A", "B", "a", "Z"], [["A", "a"], ["A", "B"], ["a", "Z"], ["B", "Z"]], "A", "Z"), {"path": ["A", "B", "Z"], "hops": 2})

    def test_19_missing_field_precedence(self):
        self.assertEqual(module.process_text('{"nodes": []}')["error"], {"code": "MISSING_FIELD", "message": "Missing required field: edges."})

    def test_20_unknown_edge_node(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A"], "edges": [["A", "B"]], "start": "A", "target": "A"}))["error"]["code"], "UNKNOWN_EDGE_NODE")


if __name__ == "__main__":
    unittest.main()
