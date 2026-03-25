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


        

