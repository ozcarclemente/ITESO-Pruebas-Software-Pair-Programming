import unittest
from password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):
    """
    Tests for the validate_password function.
    """

    def test_should_return_true_when_password_is_valid(self):
        """
        Test that the function returns True when the password is valid
        """

        # Given
        password = "Abc12345"

        # When
        result = validate_password(password)

        # Then
        self.assertTrue(result)

    def test_should_return_message_when_password_is_less_than_8_characters(self):
        """
        Test that the function returns a message when the password is less than 8 characters
        """

        # Given
        password = "Abc123"

        # When
        result = validate_password(password)

        # Then
        self.assertEqual(result, "Password must be at least 8 characters long")


    def test_should_return_message_when_password_has_less_than_2_numbers(self):
        """
        Test that the function returns a message when the password has less than 2 numbers
        """
        # Given
        password = "Password1"

        # When
        result = validate_password(password)

        # Then
        self.assertEqual(result, "The password must contain at least 2 numbers")

    def test_should_return_all_error_messages_when_multiple_validations_fail(self):
        """
        Test that the function returns all error messages separated by newlines
        when multiple validations fail
        """
 
        # Given
        password = "Abc"
 
        # When
        result = validate_password(password)
 
        # Then
        self.assertEqual(result, "Password must be at least 8 characters long\nThe password must contain at least 2 numbers")
    

    def test_should_return_message_when_password_has_no_capital_letters(self):
        """
        Test that the function returns a message when the password has no capital letters
        """
        # Given
        password = "password123"

        # When
        result = validate_password(password)

        # Then
        self.assertEqual(result, "Password must contain at least one capital letter")

    def test_should_return_message_when_password_has_no_special_characters(self):
        """
        Test that the function returns a message when the password has no special characters
        """
 
        # Given
        password = "Password12"
 
        # When
        result = validate_password(password)
 
        # Then
        self.assertEqual(result, "Password must contain at least one special character")