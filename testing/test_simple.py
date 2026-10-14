import unittest
from simple import add


class TestBasics(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2, 3), 5)

    def test2(self):
            self.assertEqual(add(2, -2), 0)

