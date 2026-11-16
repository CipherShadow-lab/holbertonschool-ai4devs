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


class TestPathFinderGroup01(unittest.TestCase):
    def test_01_direct(self):
        self.assertEqual(query(["A", "B"], [["A", "B"]], "A", "B"), {"path": ["A", "B"], "hops": 1})

    def test_02_multihop(self):
        self.assertEqual(query(["A", "B", "C"], [["A", "B"], ["B", "C"]], "A", "C"), {"path": ["A", "B", "C"], "hops": 2})
