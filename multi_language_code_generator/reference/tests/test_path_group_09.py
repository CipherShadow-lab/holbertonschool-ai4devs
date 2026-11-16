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


class TestPathFinderGroup09(unittest.TestCase):
    def test_17_self_loop(self):
        self.assertEqual(query(["A", "B"], [["A", "A"], ["A", "B"]], "A", "B"), {"path": ["A", "B"], "hops": 1})

    def test_18_case_sensitive_ascii_order(self):
        self.assertEqual(query(["A", "B", "a", "Z"], [["A", "a"], ["A", "B"], ["a", "Z"], ["B", "Z"]], "A", "Z"), {"path": ["A", "B", "Z"], "hops": 2})
