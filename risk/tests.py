from unittest import TestCase

from .countries import Country
from .continents import Continent


class TestCountry(TestCase):

    def setUp(self) -> None:
        self.country_name = "Catalunya"
        self.country = Country(self.country_name)

        self.owner = "Laia"
        self.adjacent_countries = ["Spain", "France", "Andorra"]

    def test_creation(self):
        self.assertEqual(self.country_name, str(self.country))
        self.assertEqual(0, len(self.country))

    def test_owner_without_soldiers(self):
        self.country.set_owner(self.owner, 0)
        self.country.add_soldiers(3)

    def test_owner_ok(self):
        self.country.set_owner(self.owner, 1)
        self.assertEqual(self.owner, self.country.owner)

    def test_add_soldiers_with_no_owner(self):
        self.country.add_soldiers(35)
        self.assertEqual(0, len(self.country))

    def test_add_and_remove_soldiers(self):
        self.country.set_owner(self.owner, 1)
        self.assertEqual(1, len(self.country))
        self.country.add_soldiers(24)
        self.assertEqual(25, len(self.country))
        self.country.remove_soldiers(24)
        self.assertEqual(1, len(self.country))
        self.country.remove_soldiers(1)
        self.assertEqual(0, len(self.country))
        ## The country looses the owner
        self.country.add_soldiers(5)
        self.assertEqual(0, len(self.country))

        self.country.set_owner(self.owner, 1)
        self.country.remove_soldiers(34)
        self.assertEqual(0, len(self.country))
        ## The country looses the owner
        self.country.set_owner(self.owner, 1)
        self.country.add_soldiers(3)
        self.assertEqual(4, len(self.country))

    def test_set_owner_none(self):
        self.country.set_owner(self.owner, 25)
        self.country.set_owner(None, 34)
        self.assertEqual(0, len(self.country))

    def test_adjacents(self):
        self.assertEqual(
            1, self.country.set_adjacent(self.adjacent_countries[0])
        )
        for i in range(len(self.adjacent_countries)):
            number_of_adjacents = self.country.set_adjacent(
                self.adjacent_countries[i]
            )
        self.assertEqual(len(self.adjacent_countries), number_of_adjacents)

    def test_move_soldiers_not_enough_units(self):
        self.country.set_owner(self.owner, 1)
        self.country.set_adjacent(self.adjacent_countries[0])
        self.country.move_soldiers(self.adjacent_countries[0], 1)
        self.assertEqual(1, len(self.country))

    def test_move_soldiers_not_adjacent_country(self):
        self.country.set_owner(self.owner, 2)
        self.country.move_soldiers("Unknown country", 1)
        self.assertEqual(2, len(self.country))

    def test_move_soldiers_ok(self):
        self.country.set_owner(self.owner, 2)
        self.country.set_adjacent(self.adjacent_countries[0])
        self.country.move_soldiers(self.adjacent_countries[0], 1)
        self.assertEqual(1, len(self.country))


class TestContinent(TestCase):

    def setUp(self) -> None:
        self.continent_name = "Atlantis"
        self.countries = [
            "Blind Guardian", "Gamma Ray", "Iron Maiden", "Iced Earth"
        ]
        self.continent = Continent(
            self.continent_name, self.countries
        )

        self.owner = "Laia"

    def test_creation(self):
        self.assertEqual(len(self.countries), len(self.continent))
        self.assertEqual(
            f"Continent {self.continent_name}", str(self.continent_name)
        )
        self.assertEqual(0, self.continent.get_bonus("Player name"))

    def test_get_bonus(self):
        self.assertEqual(0, self.continent.get_bonus(self.owner))
        self.continent[self.countries[0]] = self.owner, 4
        self.assertEqual(0, self.continent.get_bonus(self.owner))

        for i in range(len(self.countries)):
            self.continent[self.countries[i]] = self.owner, 3
        self.assertEqual(2, self.continent.get_bonus(self.owner))

        self.continent["Unknown country"] = self.owner, 56
        self.assertEqual(2, self.continent.get_bonus(self.owner))

    def test_get_continent_countries_owners(self):
        self.assertFalse(self.continent["Unknown country"])
        self.assertIsNone(self.continent[self.countries[0]])

        self.continent[self.countries[0]] = self.owner, 3
        self.assertEqual(self.owner, self.continent[self.countries[0]])
