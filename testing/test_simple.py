import unittest
from simple import add


class TestBasics(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
