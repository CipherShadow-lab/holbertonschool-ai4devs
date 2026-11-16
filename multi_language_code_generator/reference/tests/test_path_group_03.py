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


class TestPathFinderGroup03(unittest.TestCase):
    def test_05_same_node(self):
        self.assertEqual(query(["A"], [], "A", "A"), {"path": ["A"], "hops": 0})

    def test_06_directed(self):
        self.assertEqual(query(["A", "B"], [["A", "B"]], "B", "A"), {"path": [], "hops": None})
