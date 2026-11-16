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


class TestPathFinderGroup10(unittest.TestCase):
    def test_19_missing_field_precedence(self):
        self.assertEqual(module.process_text('{"nodes": []}')["error"], {"code": "MISSING_FIELD", "message": "Missing required field: edges."})

    def test_20_unknown_edge_node(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A"], "edges": [["A", "B"]], "start": "A", "target": "A"}))["error"]["code"], "UNKNOWN_EDGE_NODE")
