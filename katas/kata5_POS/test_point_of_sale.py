"""
Test for point of sale functionality.
"""

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
        test_cases = [
            {
                "description": "Valid barcode 12345 returns $7.25",
                "barcode": "12345",
                "expected": "$7.25",
            },
            {
                "description": "Valid barcode 23456 returns $12.50",
                "barcode": "23456",
                "expected": "$12.50",
            },
            {
                "description": "Barcode '99999' returns 'Error: Barcode not found' ",
                "barcode": "99999",
                "expected": "Error: Barcode not found",
            },
            {
                "description": "Empty barcode returns 'Error: empty Barcode'",
                "barcode": "",
                "expected": "Error: empty barcode",
            },
            {
                "description": "Two valid barcodes and total returns sum",
                "barcode": ["12345", "23456"],
                "expected": "$19.75",  # $7.25 + $12.50
            },
            {
                "description": "One valid barcode and total returns same price",
                "barcode": ["12345"],
                "expected": "$7.25",
            },
            {
                "description": "Error items are ignored in the total",
                "barcode": ["12345", "99999", "23456"],
                "expected": "$19.75",  # ignora el código no encontrado
            },
        ]

        for case in test_cases:
            with self.subTest(msg=case["description"], barcode=case["barcode"]):
                result = scan_barcode(case["barcode"])
                self.assertEqual(result, case["expected"])
