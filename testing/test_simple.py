import unittest
from simple import add, is_even, maybe_get_value

class TestBasics(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(add(2, 3), 5)

    def test_assert_true(self):
        self.assertTrue(is_even(4))

    def test_assert_is_none(self):
        self.assertIsNone(maybe_get_value(False))

if __name__ == "__main__":
    unittest.main()
