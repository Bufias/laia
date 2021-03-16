from unittest import TestCase

from .taules import Taula
from .restaurants import Restaurant
from .restaurants_covid import RestaurantCovid


class TestTaula(TestCase):

    def test_taula(self):
        t = Taula(6)
        self.assertEqual(6, t.capacitat)
        self.assertEqual(6, t.nlliures)
        self.assertEqual(0, t.ocupacio())

        self.assertTrue(t.ocupar(1))
        self.assertFalse(t.ocupar(2))

        self.assertEqual(6, t.capacitat)
        self.assertEqual(5, t.nlliures)
        self.assertEqual(1, t.ocupacio())

        t.alliberar()
        self.assertEqual(0, t.ocupacio())
        self.assertTrue(t.ocupar(5))
        self.assertEqual(1, t.nlliures)
        self.assertEqual(5, t.ocupacio())
        self.assertFalse(t.ocupar(1))
        self.assertEqual(1, t.nlliures)


class TestRestaurant(TestCase):

    def test_restaurant(self):
        r0 = Restaurant("provanom", 10)

        self.assertEqual("provanom", r0.nom)

        r = Restaurant("Ca l'Informàtica", 10)
        self.assertTrue(isinstance(r, Restaurant))
        self.assertEqual("Restaurant Ca l'Informàtica", str(r))
        self.assertEqual(10, len(r))
        self.assertEqual(0, r.capacitat())

        for i in range(5):
            r.modif_taula(i, 5)
        self.assertEqual(25, r.capacitat())
        self.assertEqual(0, r.ocupacio())

        for i in range(5):
            r[i] = 5
        self.assertEqual(25, r.ocupacio())
        self.assertEqual(25, r.capacitat())

        for i in range(5, 10):
            r.modif_taula(i, 4)
        self.assertEqual(45, r.capacitat())
        self.assertEqual(25, r.ocupacio())

        for i in range(5, 10):
            r[i] = 2
        self.assertEqual(45, r.capacitat())
        self.assertEqual(35, r.ocupacio())

        r.modif_taula(0, 15)
        self.assertEqual(55, r.capacitat())

        r[0] = 1
        self.assertEqual(31, r.ocupacio())

        r[0] = 4
        self.assertEqual(31, r.ocupacio())

        r.modif_taula(0, 15)
        self.assertEqual(30, r.ocupacio())

        r[0] = 15
        self.assertEqual(45, r.ocupacio())


class TestRestaurantCovid(TestCase):

    def test_restaurant_covid(self):
        r3 = RestaurantCovid('Casa LR1', 5, 50)
        self.assertTrue(
            isinstance(r3, RestaurantCovid) and isinstance(r3, Restaurant)
        )

        self.assertEqual('Casa LR1', r3.nom)
        self.assertEqual('Restaurant Casa LR1', str(r3))
        self.assertEqual(50, r3.maxafor)
        self.assertEqual(5, len(r3))

        for i in range(5):
            r3.modif_taula(i, 10)
        self.assertEqual(50, r3.capacitat())

        r4 = RestaurantCovid('Casa LR1 red', 5, 20)
        self.assertTrue(
            isinstance(r4, RestaurantCovid), isinstance(r4, Restaurant)
        )
        self.assertEqual(20, r4.maxafor)
        for i in range(5):
            r4.modif_taula(i, 10)
        self.assertEqual(20, r4.capacitat())

        r5 = RestaurantCovid('Casa LR1 red', 5, 200)
        self.assertTrue(
            isinstance(r5, RestaurantCovid), isinstance(r5, Restaurant)
        )
        self.assertEqual(r5.maxafor, 200)
        for i in range(5):
            r5.modif_taula(i, 10)
        self.assertEqual(50, r5.capacitat())
