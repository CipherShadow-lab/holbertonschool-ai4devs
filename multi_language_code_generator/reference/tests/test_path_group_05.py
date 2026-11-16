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


class TestPathFinderGroup05(unittest.TestCase):
    def test_09_unsorted_edges(self):
        self.assertEqual(query(["A", "B", "C", "D"], [["C", "D"], ["A", "C"], ["B", "D"], ["A", "B"]], "A", "D"), {"path": ["A", "B", "D"], "hops": 2})

    def test_10_disconnected(self):
        self.assertEqual(query(["A", "B", "C"], [["A", "B"]], "A", "C"), {"path": [], "hops": None})
