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

    def test_should_handle_newlines_between_numbers(self):
        """
        Test that the function can handle newlines between numbers
        """

        # Given
        numbers = "1\n2,3"

        # When
        result = add(numbers)

        # Then
        self.assertEqual(result, 6)

    def test_should_raise_error_when_separator_is_at_the_end(self):
        """
        Test that the function raises an error when the input ends with a separator
        """

        # Given
        numbers = "1,2,3,"

        # When / Then
        with self.assertRaises(ValueError):
            add(numbers)


    def test_custom_single_character_delimiter(self):
        """
        Escenario: "//;\n1;3" -> 4
        """
        self.assertEqual(add("//;\n1;3"), 4)


    def test_custom_multi_character_delimiter(self):
        """
        Escenario: "//sep\n2sep5" -> 7
        """
        self.assertEqual(add("//sep\n2sep5"), 7)


    def test_custom_delimiter_with_invalid_separator_should_raise_error(self):
        """
        Escenario: "//|\n1|2,3" -> Debería lanzar error porque se usó ',' en lugar de '|'
        """
        
        with self.assertRaisesRegex(ValueError, r"'\|' expected but ',' found"):
            add("//|\n1|2,3")


    def test_should_raise_error_when_negative_numbers_are_given(self):
        """
        Test that the function raises an error when negative numbers are given
        """

        # Given
        numbers = "1,-2,3"

        # When / Then
        with self.assertRaisesRegex(ValueError, "Negative number\(s\) not allowed: -2"):
            add(numbers)

    
    def test_multiple_errors_should_be_collected_and_separated_by_newlines(self):
        """
        Escenario: "//|\n1|2,-3" -> Debe juntar el error de negativo y el de separador inválido
        """
        # Given
        numbers = "//|\n1|2,-3"
        expected_message = "Negative number(s) not allowed: -3\n'|' expected but ',' found at position 3."

        # When / Then
        with self.assertRaises(ValueError) as context:
            add(numbers)

        # mensaje de excepcion con ambas lineas
        self.assertEqual(str(context.exception), expected_message)
