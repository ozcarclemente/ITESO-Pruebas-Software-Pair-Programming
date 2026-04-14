"""
Tests for the banking kata.
"""

import json
import os
import unittest
from io import StringIO
from unittest.mock import patch

from account import Account


class TestAccount(unittest.TestCase):
    """
    Tests for the Account class.
    """

    def test_account_operations_data_driven(self):
        """
        Data driven tests for deposit, withdraw, and print statement.
        """
        base_dir = os.path.dirname(__file__)
        data_file = os.path.join(base_dir, "data.json")

        # Load test cases from data.json
        with open(data_file, "r", encoding="utf-8") as f:
            test_cases = json.load(f)

        for case in test_cases:
            with self.subTest(msg=case["description"]):
                account = Account()

                for operation, amount, date in case["operations"]:
                    with patch("account.datetime") as mock_date:
                        mock_date.today.return_value.strftime.return_value = date

                        if operation == "deposit":
                            account.deposit(amount)
                        elif operation == "withdraw":
                            account.withdraw(amount)

                with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                    account.print_statement()
                    output = mock_stdout.getvalue().strip()

                self.assertEqual(output, case["expected_output"])
