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


class TestPathFinderGroup08(unittest.TestCase):
    def test_15_invalid_name(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A-B"], "edges": [], "start": "A-B", "target": "A-B"}))["error"]["code"], "INVALID_NODE_NAME")

    def test_16_duplicate_nodes(self):
        self.assertEqual(module.process_text(json.dumps({"nodes": ["A", "A"], "edges": [], "start": "A", "target": "A"}))["error"]["code"], "DUPLICATE_NODE")
