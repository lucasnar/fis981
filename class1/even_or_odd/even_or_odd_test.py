import unittest
from even_or_odd import ParityChecker

class ParityCheckerTest(unittest.TestCase):
    def test_is_even_for_even_numbers(self):
        number = -2
        is_even = ParityChecker(number).is_even()
        self.assertEqual(is_even, True)

        number = 0
        is_even = ParityChecker(number).is_even()
        self.assertEqual(is_even, True)

        number = 42
        is_even = ParityChecker(number).is_even()
        self.assertEqual(is_even, True)

    def test_is_even_for_odd_numbers(self):
        number = 3
        is_even = ParityChecker(number).is_even()
        self.assertEqual(is_even, False)

        number = -63
        is_even = ParityChecker(number).is_even()
        self.assertEqual(is_even, False)

    def test_parity_name(self):
        number = 3
        parity_name = ParityChecker(number).parity_name()
        self.assertEqual(parity_name, "ímpar")

        number = 2
        parity_name = ParityChecker(number).parity_name()
        self.assertEqual(parity_name, "par")

if __name__ == '__main__':
    unittest.main()
