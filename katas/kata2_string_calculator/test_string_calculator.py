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

    
    def test_should_allow_add_to_handle_an_unknown_number_of_arguments(self):
        """
        Test that the function can handle an unknown number of arguments
        """

        # Given
        numbers = "1,2,3,4,5"

        # When
        result = add(numbers)

        # Then
        self.assertEqual(result, 15)


