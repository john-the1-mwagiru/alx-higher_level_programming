import unittest

print_square = __import__("6-max_integer").max_integer


class TestMaxIntger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(print_square([3, 1, 7, 4]), 7)
        self.assertEqual(print_square([-1, -3, -10, 0]), 0)

    def test_values(self):
        self.assertRaises(TypeError, print_square, 10)
