import unittest

from suma_multiplica.solution import suma_succ


class SumaMultiplicaTest(unittest.TestCase):
    def test_0(self):
        n = 10
        expected = 13

        res = suma_succ(n)

        self.assertEqual(expected, res)

    def test_1(self):
        n = 12
        expected = 23

        res = suma_succ(n)

        self.assertEqual(expected, res)

    def test_2(self):
        n = 100
        expected = 118

        res = suma_succ(n)

        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
