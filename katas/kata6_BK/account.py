"""
Implement a simple bank account class with deposit, withdraw, and print_statement methods.
"""

from datetime import datetime


class Account:
    """
    A simple bank account class that supports deposits, withdrawals, and printing statements.
    """

    def __init__(self):
        self._transactions = []
        self._balance = 0

    def _today(self):
        return datetime.today().strftime("%d/%m/%Y")

    def deposit(self, amount: int):
        """
        Deposits the specified amount into the account.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self._balance += amount
        self._transactions.append(
            {
                "date": self._today(),
                "amount": float(amount),
                "balance": float(self._balance),
            }
        )

    def withdraw(self, amount: int):
        """
        Withdraws the specified amount from the account.
        """

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount
        self._transactions.append(
            {
                "date": self._today(),
                "amount": float(-amount),
                "balance": float(self._balance),
            }
        )

    def print_statement(self):
        """
        Prints the account statement.
        """
        print("DATE | AMOUNT | BALANCE")
        for transaction in reversed(self._transactions):
            print(
                f"{transaction['date']} | "
                f"{transaction['amount']:.2f} | "
                f"{transaction['balance']:.2f}"
            )
