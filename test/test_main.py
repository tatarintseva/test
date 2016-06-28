__author__ = 'otatarintseva'

import unittest
from main import fib


class TestFib(unittest.TestCase):

    def test_first(self):
        self.assertEqual(fib(1), 1)

    def test_third(self):
        self.assertEqual(fib(3), 2)

    def test_38(self):
        self.assertEqual(fib(38), 39088169)

    def test0(self):
        self.assertIsNone(fib(0))
