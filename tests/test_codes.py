import unittest

from invites import Invite, generate_code, is_valid


class GenerateCodeTest(unittest.TestCase):
    def test_code_has_eight_characters(self):
        self.assertEqual(len(generate_code()), 8)


class IsValidTest(unittest.TestCase):
    def test_matching_code_is_valid(self):
        self.assertTrue(is_valid(Invite(code="AB12CD34"), "AB12CD34"))

    def test_used_code_is_rejected(self):
        self.assertFalse(is_valid(Invite(code="AB12CD34", used=True), "AB12CD34"))


if __name__ == "__main__":
    unittest.main()
