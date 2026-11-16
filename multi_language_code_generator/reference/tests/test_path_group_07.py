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


class TestPathFinderGroup07(unittest.TestCase):
    def test_13_invalid_json(self):
        self.assertEqual(module.process_text("{" )["error"]["code"], "INVALID_JSON")

    def test_14_invalid_edge_shape(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A"], "edges": [["A"]], "start": "A", "target": "A"}))["error"]["code"], "INVALID_EDGE")
