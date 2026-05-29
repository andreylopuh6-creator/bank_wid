import unittest

from src.masks import get_mask_account, get_mask_card_number


class TestMasks(unittest.TestCase):

    def test_get_mask_card_number_valid(self):
        self.assertEqual(
            get_mask_card_number("1234567812345678"), "1234 56** **** 5678"
        )
        self.assertEqual(
            get_mask_card_number("1234-5678-1234-5678"), "1234 56** **** 5678"
        )

    def test_get_mask_card_number_invalid(self):
        with self.assertRaises(ValueError):
            get_mask_card_number("12345678")  # Слишком короткий
        with self.assertRaises(ValueError):
            get_mask_card_number("123456781234567890")  # Слишком длинный

    def test_get_mask_account_valid(self):
        self.assertEqual(get_mask_account("123456789012"), "**9012")
        self.assertEqual(get_mask_account("1234-5678-9012"), "**9012")
        self.assertEqual(get_mask_account("1234"), "**1234")

    def test_get_mask_account_invalid(self):
        with self.assertRaises(ValueError):
            get_mask_account("123")  # Слишком короткий


if __name__ == "__main__":
    unittest.main()
