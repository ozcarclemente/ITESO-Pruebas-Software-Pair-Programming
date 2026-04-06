import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    """
    Tests for the fizzbuzz function.
    """

    def test_should_return_number_as_string(self):
        """
        Test that the function returns the number as a string
        """

        # Given
        number = 1

        # When
        result = fizzbuzz(number)

        # Then
        self.assertEqual(result, "1")

    def test_multiple_of_3_should_return_fizz(self):
        """
        Test that the function returns "Fizz" when the number is a multiple of 3
        """

        # Given
        number = 9

        # When
        result = fizzbuzz(number)

        # Then
        self.assertEqual(result, "Fizz")


        

