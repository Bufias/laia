from unittest import TestCase

from .sanefa import sanefa
from .s_eol import suma_EOL
from .elimina import elimina


class TestSanefa(TestCase):

    def test_1(self):
        res = sanefa(10, 3)
        expected = [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
        self.assertEqual(expected, res)

    def test_2(self):
        res = sanefa(8, 1)
        expected = [0, 1, 0, 1, 0, 1, 0, 1]
        self.assertEqual(expected, res)


class TestEOL(TestCase):

    def test_1(self):
        expected = 8
        res = suma_EOL(8)
        self.assertEqual(expected, res)

    def test_2(self):
        expected = 6
        res = suma_EOL([1, 2, 3])
        self.assertEqual(expected, res)

    def test_3(self):
        expected = 31
        res = suma_EOL([7, [12], [5, 7]])
        self.assertEqual(expected, res)

    def test_4(self):
        expected = 133
        res = suma_EOL([7, [12], [5, 7]])
        self.assertEqual(expected, res)

    def test_5(self):
        expected = 0
        res = suma_EOL([])
        self.assertEqual(expected, res)


class TestElimina(TestCase):
    def test_1(self):
        expected = [2, 4, 16, 22, 11, 2]
        res = elimina([2, 4, 8, 16, 22, 8, 11, 2], 8)
        self.assertEqual(expected, res)

    def test_2(self):
        expected = [2, 4, 8, 16, 22, 8, 11, 2]
        res = elimina([2, 4, 8, 16, 22, 8, 11, 2], 100)
        self.assertEqual(expected, res)

    def test_3(self):
        expected = []
        res = elimina([1, 1, 1, 1, 1, 1], 1)
        self.assertEqual(expected, res)
