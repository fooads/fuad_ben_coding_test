import unittest

class TestRegistrationForm(unittest.TestCase):


    # Functional Test Cases
    def test_valid_registration(self):
        # Test a valid registration case
        result = register_account("validusername", "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 200)
        self.assertEqual(result["msg"], "success")

    def test_invalid_username(self):
        # Test with an invalid username
        result = register_account("invalid username", "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "invalid_username: no_spaces_allowed")

    def test_invalid_password(self):
        # Test with a short password
        result = register_account("validusername", "aaa", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "invalid_password: must_be_at_least_8_characters")

    def test_invalid_email_format(self):
        # Test with an invalid email format
        result = register_account("validusername", "SecurePassword123!", "fuad.com", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "invalid_email_format")

    def test_newsletter_checkbox(self):
        # Test with newsletter checkbox
        result = register_account("validusername", "SecurePassword123!", "user@fuad.kr", False)
        self.assertEqual(result["status_code"], 200)
        self.assertEqual(result["msg"], "registration_successful")

        result = register_account("validusername", "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 200)
        self.assertEqual(result["msg"], "success")


    # Boundary Test Cases
    def test_username_minimum_length(self):
        # Assuming minimum username length is 5
        result = register_account("userr", "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 200)
        self.assertEqual(result["msg"], "success")

    def test_username_below_minimum_length(self):
        # Username is shorter than minimum length
        result = register_account("us", "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "invalid_username: must_be_at_least_3_characters")

    def test_password_minimum_length(self):
        # Assuming minimum password length is 8
        result = register_account("validusername", "12345678", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 200)
        self.assertEqual(result["msg"], "success")

    def test_password_below_minimum_length(self):
        # Password is shorter than minimum length
        result = register_account("validusername", "1234567", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "invalid_password: must_be_at_least_8_characters")


    # Edge Cases
    def test_empty_username(self):
        # Username is empty
        result = register_account("", "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "username_cannot_be_empty")

    def test_empty_password(self):
        # Password is empty
        result = register_account("validusername", "", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "password_cannot_be_empty")

    def test_empty_email(self):
        # Email is empty
        result = register_account("validusername", "SecurePassword123!", "", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "email_cannot_be_empty")

    def test_special_characters_in_username(self):
        # Username with special characters
        result = register_account("user!@#", "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "invalid_username: special_characters_not_allowed")

    def test_invalid_email_edge_case(self):
        # Edge case email
        result = register_account("validusername", "SecurePassword123!", "user@", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "invalid_email_format")

    def test_max_length_username(self):
        # Assuming maximum length for username is 15 characters
        result = register_account("a" * 15, "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 200)
        self.assertEqual(result["msg"], "success")

    def test_above_max_length_username(self):
        # Username exceeding maximum length
        result = register_account("a" * 16, "SecurePassword123!", "user@fuad.kr", True)
        self.assertEqual(result["status_code"], 400)
        self.assertEqual(result["msg"], "invalid_username: maximum_length_is_15_characters")


if __name__ == "__main__":
    unittest.main()
