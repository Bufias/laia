import unittest

from successio_x_i.solution import successio


class SolutionTest(unittest.TestCase):
    def test_1(self):
        res = successio(0.09, 0.001)
        self.assertEqual(6, res)

    def test_2(self):
        res = successio(0, 0.01)
        self.assertEqual(96, res)

    def test_3(self):
        res = successio(0.06, 0.001)
        self.assertEqual(12, res)

    def test_4(self):
        res = successio(0, 0.001)
        self.assertEqual(996, res)


if __name__ == '__main__':
    unittest.main()
