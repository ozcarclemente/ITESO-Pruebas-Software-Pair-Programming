"""
Test for point of sale functionality.
"""

import json
import os
import unittest

from point_of_sale import scan_barcode


class TestPointOfSale(unittest.TestCase):
    """
    Test for scan_barcode function.
    """

    def test_scan_barcode_data_driven(self):
        """
        Data driven tests for scanning single barcodes and handling errors.
        """
        base_dir = os.path.dirname(__file__)
        data_file = os.path.join(base_dir, "data.json")

        with open(data_file, "r", encoding="utf-8") as file:
            test_cases = json.load(file)

        for case in test_cases:
            with self.subTest(msg=case["description"], barcode=case["barcode"]):
                result = scan_barcode(case["barcode"])
                self.assertEqual(result, case["expected"])
