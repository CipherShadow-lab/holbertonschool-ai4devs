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


class TestPathFinderGroup02(unittest.TestCase):
    def test_03_tie(self):
        self.assertEqual(query(["A", "B", "C", "D"], [["A", "C"], ["A", "B"], ["C", "D"], ["B", "D"]], "A", "D"), {"path": ["A", "B", "D"], "hops": 2})

    def test_04_no_path(self):
        self.assertEqual(query(["A", "B"], [], "A", "B"), {"path": [], "hops": None})
