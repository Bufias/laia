from unittest import TestCase

from .restaurants import Restaurant
from .mesrest import cerca_taula


class TestRestaurant(TestCase):

    def setUp(self) -> None:
        self.r = Restaurant('La Perdiu Roja', 10)

    def test_name(self):
        self.assertEqual('Restaurant La Perdiu Roja', str(self.r))

    def test_tables(self):
        self.assertEqual(10, len(self.r))

    def test_reserves(self):
        for i in range(5):
            self.r.modif_taula(i, 4)

        self.r.modif_taula(5, 6)

        for i in range(6, 10):
            self.r.modif_taula(i, 8)

        for i in range(2, 8):
            self.r[i] = 2

        res_cerca = cerca_taula(self.r, 3)
        self.assertEqual(0, res_cerca)

        self.assertTrue(self.r[0] == 3)

        res_cerca = cerca_taula(self.r, 5)
        self.assertEqual(8, res_cerca)

        self.assertTrue(self.r[8] == 5)

        res_cerca = cerca_taula(self.r, 9)
        self.assertEqual(-1, res_cerca)

        self.assertEqual(
            [3, 0, 2, 2, 2, 2, 2, 2, 5, 0], [self.r[i] for i in range(10)]
        )