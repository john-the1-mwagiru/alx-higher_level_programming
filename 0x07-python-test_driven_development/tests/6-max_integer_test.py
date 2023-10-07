import unittest

"""Unittests for max_integer()"""

max_integer = __import__("6-max_integer").max_integer


class TestMaxIntger(unittest.TestCase):
    """Defines unittests for max_integer()"""

    def test_max(self):
        """Tests a normal list"""
        self.assertEqual(max_integer([3, 1, 7, 4]), 7)
        self.assertEqual(max_integer([-1, -3, -10, 0]), 0)

    def test_floats(self):
        """Tests a list of floats"""
        self.assertEqual(max_integer([1.1, 1.0, 7.7, 9.8]), 9.8)

    def test_floats_and_ints(self):
        """Tests a list of floats and integers"""
        self.assertEqual(max_integer([9.9, 30, 29.9]), 30)

    def test_strings(self):
        """Tests strings"""
        self.assertEqual(max_integer("John"), "o")

    def test_empty_strings(self):
        """Tests empty strings"""
        self.assertEqual(max_integer(""), None)

    def test_empty_list(self):
        """Tests an empty list"""
        self.assertEqual(max_integer([]), None)
