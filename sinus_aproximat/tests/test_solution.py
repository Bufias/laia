import unittest

from sinus_aproximat.solution import sinus_aproximat


class SinusAproximatTest(unittest.TestCase):
    def test_sinus_aproximat_003(self):
        res = sinus_aproximat(0.03, 0.01)
        expected = 0.03
        self.assertEqual(expected, round(res, 2))

    def test_sinus_aproximat_0_3(self):
        res = sinus_aproximat(0.3, 0.01)
        expected = 0.3
        self.assertEqual(expected, round(res, 2))

    def test_sinus_aproximat_0_1(self):
        res = sinus_aproximat(0.1, 0.0001)
        expected = 0.09983
        self.assertEqual(expected, round(res, 5))

    def test_1_exp_minus_5(self):
        res = sinus_aproximat(0.3, 1e-5)
        expected = 0.29552025
        self.assertEqual(expected, round(res, 8))


if __name__ == '__main__':
    unittest.main()
