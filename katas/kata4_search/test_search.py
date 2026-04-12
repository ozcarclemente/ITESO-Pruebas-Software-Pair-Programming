"""
Test for search functionality.
"""

import json
import os
import unittest

from search import search


class TestSearch(unittest.TestCase):
    """
    Tests for search function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class for tests.
        """
        path = os.path.join(os.path.dirname(__file__), "cities.json")
        with open(path, "r", encoding="utf-8") as f:
            cls.cities = json.load(f)["cities"]

    def test_search_cities_data_driven(self):
        """
        Data driven tests for search function.
        """

        test_cases = [
            {
                "test_case": "less than 2 characters returns empty list",
                "input": "a",
                "expected": [],
            },
            {
                "test_case": "finds matches by prefix",
                "input": "Va",
                "expected": ["Valencia", "Vancouver"],
            },
            {
                "test_case": "search is case insensitive",
                "input": "va",
                "expected": ["Valencia", "Vancouver"],
            },
            {
                "test_case": "finds matches by substring",
                "input": "ape",
                "expected": ["Budapest"],
            },
            {
                "test_case": "asterisk returns all cities",
                "input": "*",
                "expected": self.cities,
            },
            {
                "test_case": "no matches returns empty list",
                "input": "xyz",
                "expected": [],
            },
        ]

        for case in test_cases:
            with self.subTest(case=case["test_case"], input=case["input"]):
                result = search(case["input"])
                self.assertEqual(case["expected"], result)
