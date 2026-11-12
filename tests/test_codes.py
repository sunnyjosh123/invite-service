import unittest
from datetime import datetime, timedelta

from invites import Invite, generate_code, is_valid

CREATED = datetime(2026, 11, 1, 10, 0)


class GenerateCodeTest(unittest.TestCase):
    def test_code_has_eight_characters(self):
        self.assertEqual(len(generate_code()), 8)


class IsValidTest(unittest.TestCase):
    def test_matching_code_is_valid(self):
        invite = Invite(code="AB12CD34", created_at=CREATED)
        self.assertTrue(is_valid(invite, "AB12CD34", CREATED + timedelta(days=1)))

    def test_used_code_is_rejected(self):
        invite = Invite(code="AB12CD34", created_at=CREATED, used=True)
        self.assertFalse(is_valid(invite, "AB12CD34", CREATED + timedelta(days=1)))

    def test_code_is_valid_on_day_six(self):
        invite = Invite(code="AB12CD34", created_at=CREATED)
        self.assertTrue(is_valid(invite, "AB12CD34", CREATED + timedelta(days=6)))

    def test_code_is_rejected_after_seven_days(self):
        invite = Invite(code="AB12CD34", created_at=CREATED)
        later = CREATED + timedelta(days=7, hours=1)
        self.assertFalse(is_valid(invite, "AB12CD34", later))


if __name__ == "__main__":
    unittest.main()
