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

        # Get the directory of the current file
        path = os.path.dirname(__file__)

        # Load cities from cities.json
        cities_file = os.path.join(path, "cities.json")
        with open(cities_file, "r", encoding="utf-8") as f:
            cls.cities = json.load(f)["cities"]

        # Load test cases from test.json
        test_data = os.path.join(path, "test.json")
        with open(test_data, "r", encoding="utf-8") as f:
            cls.test_cases = json.load(f)

    def test_search_cities_data_driven(self):
        """
        Data driven tests for search function.
        """

        for case in self.test_cases:
            with self.subTest(case=case["test_case"], input=case["input"]):
                result = search(case["input"])

                expected = case["expected"]

                if expected == "ALL_CITIES":
                    expected = self.cities

                self.assertEqual(expected, result)
