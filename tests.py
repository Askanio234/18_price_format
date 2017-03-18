import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):
    def test_case_without_decimal_part(self):
        self.assertEqual(format_price("3245.000000"), "3 245")

    def test_case_with_decimal_part(self):
        self.assertEqual(format_price("12345.67"), "12 345.67")

    def test_case_with_multiple_thousands_separators(self):
        self.assertEqual(format_price("123456789"), "123 456 789")

    def test_case_with_string_zero_and_valid_decinal_part(self):
        self.assertEqual(format_price("0.990000"), "0.99")

    def test_case_with_string_zero(self):
        self.assertEqual(format_price("0"), "n/a")

    def test_case_with_string_zero_and_zero_decimal_part(self):
        self.assertEqual(format_price("0.000000"), "n/a")

    def test_case_with_nonconvertable_string(self):
        self.assertEqual(format_price("nope"), "n/a")

    def test_case_with_none(self):
        self.assertEqual(format_price(None), "n/a")

    def test_case_with_integer(self):
        self.assertEqual(format_price(3245), "3 245")

    def test_case_with_integer_zero(self):
        self.assertEqual(format_price(0), "n/a")

    def test_case_with_bool(self):
        self.assertEqual(format_price(False), "n/a")

    def test_case_with_iterable(self):
        self.assertEqual(format_price(["123456", 12345]), "n/a")


if __name__ == '__main__':
    unittest.main()
