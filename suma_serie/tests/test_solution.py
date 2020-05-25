import unittest

from suma_serie.solution import suma_serie


class SumaSerieTest(unittest.TestCase):

    def test_0(self):
        x = 0.5
        eps = 0.1
        expected = 0.75

        res = suma_serie(x, eps)
        self.assertEqual(expected, round(res, 2))

    def test_1(self):
        x = 0.5
        eps = 0.01
        expected = 0.8

        res = suma_serie(x, eps)
        self.assertEqual(expected, round(res, 2))

    def test_2(self):
        x = 0.7
        eps = 0.1
        expected = 0.63

        res = suma_serie(x, eps)
        self.assertEqual(expected, round(res, 2))

    def test_3(self):
        x = 0.7
        eps = 0.01
        expected = 0.68

        res = suma_serie(x, eps)
        self.assertEqual(expected, round(res, 2))

    def test_4(self):
        x = 0.8
        eps = 0.01
        expected = 0.61

        res = suma_serie(x, eps)
        self.assertEqual(expected, round(res, 2))


if __name__ == '__main__':
    unittest.main()
