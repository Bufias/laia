from unittest import TestCase

from .sanefa import sanefa


class TestSanefa(TestCase):

    def test_1(self):
        res = sanefa(10, 3)
        expected = [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
        self.assertEqual(expected, res)

    def test_2(self):
        res = sanefa(8, 1)
        expected = [0, 1, 0, 1, 0, 1, 0, 1]
        self.assertEqual(expected, res)
