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
