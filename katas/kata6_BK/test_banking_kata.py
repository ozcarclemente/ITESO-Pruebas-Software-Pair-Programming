"""
Tests for the banking kata.
"""

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
        test_cases = [
            {
                "description": "Deposit 1000 should print statement with one transaction",
                "operations": [
                    ("deposit", 1000, "01/04/2014"),
                ],
                "expected_output": (
                    "DATE | AMOUNT | BALANCE\n" "01/04/2014 | 1000.00 | 1000.00"
                ),
            },
            {
                "description": "Deposit 1000 then withdraw 100 "
                "should print two transactions in reverse order",
                "operations": [
                    ("deposit", 1000, "01/04/2014"),
                    ("withdraw", 100, "02/04/2014"),
                ],
                "expected_output": (
                    "DATE | AMOUNT | BALANCE\n"
                    "02/04/2014 | -100.00 | 900.00\n"
                    "01/04/2014 | 1000.00 | 1000.00"
                ),
            },
            {
                "description": "Deposit 1000, withdraw 100, "
                "deposit 500 should print three transactions in reverse order",
                "operations": [
                    ("deposit", 1000, "01/04/2014"),
                    ("withdraw", 100, "02/04/2014"),
                    ("deposit", 500, "10/04/2014"),
                ],
                "expected_output": (
                    "DATE | AMOUNT | BALANCE\n"
                    "10/04/2014 | 500.00 | 1400.00\n"
                    "02/04/2014 | -100.00 | 900.00\n"
                    "01/04/2014 | 1000.00 | 1000.00"
                ),
            },
        ]

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
