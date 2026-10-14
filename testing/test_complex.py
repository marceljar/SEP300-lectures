import unittest
from complex import add, square, is_even, maybe_get_value

class TestBasics(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2, 3), 5)

    def test2(self):
            self.assertEqual(square( 3), 9)

    def test3(self):
            self.assertEqual(square(add(2, 3)), 25)

    def test4(self):
        self.assertTrue(is_even(4))

    def test5(self):
            self.assertFalse(is_even(3))

    def test6(self):
        self.assertIsNone(maybe_get_value(False))

