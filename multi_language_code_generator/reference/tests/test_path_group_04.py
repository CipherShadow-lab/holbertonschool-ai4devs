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


class TestPathFinderGroup04(unittest.TestCase):
    def test_07_cycle(self):
        self.assertEqual(query(["A", "B", "C", "D"], [["A", "B"], ["B", "C"], ["C", "A"], ["C", "D"]], "A", "D"), {"path": ["A", "B", "C", "D"], "hops": 3})

    def test_08_duplicates(self):
        self.assertEqual(query(["A", "B"], [["A", "B"], ["A", "B"]], "A", "B"), {"path": ["A", "B"], "hops": 1})
