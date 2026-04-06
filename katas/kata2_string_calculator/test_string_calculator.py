import unittest
from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    """
    Tests for the add function.
    """

    def test_should_return_zero_when_input_is_empty_string(self):
        """
        Test that the function returns 0 when the input is an empty string
        """

        # Given
        numbers = ""

        # When
        result = add(numbers)

        # Then
        self.assertEqual(result, 0)

    def test_should_return_its_value_when_only_one_number_is_given(self):
        """
        Test that the function returns the number itself when only one number is given
        """

        # Given
        numbers = "1"

        # When
        result = add(numbers)

        # Then
        self.assertEqual(result, 1)

    def test_should_return_their_sum_when_separated_by_comma(self):
        """
        Test that the function returns the sum of two numbers separated by a comma
        """

        # Given
        numbers = "1,2"

        # When
        result = add(numbers)

        # Then
        self.assertEqual(result, 3)


