import unittest
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """
    Tests for the fizzbuzz function.
    """

    def test_should_return_number_as_string_when_number_is_not_multiple_of_3_or_5(self):
        """
        Test that the function returns the number as a string when it is not a multiple of 3 or 5
        """

        # Given
        number = 1

        # When
        result = fizzbuzz(number)

        # Then
        self.assertEqual(result, "1")

    def test_should_return_fizz_when_number_is_multiple_of_3(self):
        """
        Test that the function returns "Fizz" when the number is a multiple of 3
        """

        # Given
        number = 9

        # When
        result = fizzbuzz(number)

        # Then
        self.assertEqual(result, "Fizz")

    def test_should_return_buzz_when_number_is_multiple_of_5(self):
        """
        Test that the function returns "Buzz" when the number is a multiple of 5
        """

        # Given
        number = 10

        # When
        result = fizzbuzz(number)

        # Then
        self.assertEqual(result, "Buzz")

    def test_should_return_fizzbuzz_when_number_is_multiple_of_3_and_5(self):
        """
        Test that the function returns "FizzBuzz" when the number is a multiple of 3 and 5
        """

        # Given
        number = 15

        # When
        result = fizzbuzz(number)

        # Then
        self.assertEqual(result, "FizzBuzz")
