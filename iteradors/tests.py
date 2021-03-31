from unittest import TestCase

from .primers import primers, sense_uns, n_uns


class TestPrimers(TestCase):

    def test_primers(self):
        expected = [
            7, 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            23, 3, 1, 1, 1, 1, 1, 1
        ]
        it = primers()

        results = []
        for i in range(30):
            results.append(next(it))

        self.assertEqual(expected, results)

    def test_sense_uns(self):
        expected = [2, 3, 11, 12, 12, 45, 67, 44, 45, 67, 89, 2]
        seq = iter(
            [
                1, 2, 3, 1, 1, 11, 12, 12, 1, 1, 1, 45, 67, 1, 1, 1, 1, 44,
                45, 67, 89, 2, 1, 1, 1, 1, 1
            ]
        )
        it = sense_uns(seq)

        res = []
        for i in range(12):
            res.append(next(it))

        self.assertEqual(expected, res)

    def test_primers_sense_uns(self):
        expected = [
            7, 5, 3, 11, 3, 23, 3, 47, 3, 5, 3, 101, 3, 7, 11, 3, 13, 233, 3,
            467
        ]

        it = sense_uns(primers())
        res = []
        for i in range(20):
            res.append(next(it))

        self.assertEqual(expected, res)

    def test_n_uns(self):
        expected = [1, 2, 3, 4, 5]
        seq = iter(
            [
                1, 2, 3, 1, 1, 11, 12, 12, 1, 1, 1, 45, 67, 1, 1, 1, 1, 44,
                45, 67, 89, 2, 1, 1, 1, 1, 1
            ]
        )

        it = n_uns(seq)

        self.assertEqual(expected, list(it))

    def test_n_uns_primers(self):
        expected = [
            3, 4, 10, 22, 1, 49, 2, 4, 5, 115, 232, 1, 469, 2, 943, 1888, 3778,
            5, 7564, 25
        ]
        it = n_uns(primers())

        res = []
        for i in range(20):
            res.append(next(it))

        self.assertEqual(expected, res)
