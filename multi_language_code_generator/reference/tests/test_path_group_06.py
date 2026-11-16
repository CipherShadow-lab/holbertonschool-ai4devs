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


class TestPathFinderGroup06(unittest.TestCase):
    def test_11_unknown_node(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A"], "edges": [], "start": "A", "target": "Z"})), {"error": {"code": "UNKNOWN_NODE", "message": "Start or target node does not exist."}})

    def test_12_empty_graph(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": [], "edges": [], "start": "A", "target": "B"})), {"error": {"code": "INVALID_NODES", "message": "Nodes must be a non-empty array."}})
