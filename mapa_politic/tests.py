from unittest import TestCase
import networkx as nx

from .mapes import fusiona_zones, zones_de_pas


class TestMapes(TestCase):

    def setUp(self) -> None:
        self.gm = nx.Graph()

        self.original_countries_list = [
            'Besnac', 'Ashari', 'Samari', 'Krko', 'Grenola', 'Miland',
            'Loweh', 'Filite'
        ]
        nodes_list = [
            ('Besnac', 'Grenola'),
            ('Besnac', 'Ashari'),
            ('Besnac', 'Krko'),
            ('Grenola', 'Samari'),
            ('Grenola', 'Krko'),
            ('Grenola', 'Ashari'),
            ('Grenola', 'Miland'),
            ('Miland', 'Loweh'),
            ('Miland', 'Samari'),
            ('Ashari', 'Samari')
        ]
        self.gm.add_nodes_from(self.original_countries_list)
        self.gm.add_edges_from(nodes_list)

    def test_fusiona_zones(self):
        z1 = 'Ashari'
        z2 = 'Samari'
        new_zone = 'Ashamari'
        z1_neighbours = list(self.gm.neighbors(z1))
        z2_neighbours = list(self.gm.neighbors(z2))

        expected_new_neighbours = set(z1_neighbours + z2_neighbours)
        expected_new_neighbours.remove(z1)
        expected_new_neighbours.remove(z2)

        fusiona_zones(self.gm, z1, z2, new_zone)

        new_nodes = list(self.gm.nodes)

        expected_nodes = [
            country for country in self.original_countries_list
            if country not in [z1, z2]
        ]
        expected_nodes.append(new_zone)
        self.assertEqual(sorted(new_nodes), sorted(expected_nodes))

        self.assertTrue(z1 not in new_nodes)
        self.assertTrue(z2 not in new_nodes)
        self.assertTrue(new_zone in new_nodes)

        new_zone_neighbours = list(self.gm.neighbors(new_zone))
        self.assertEqual(
            sorted(new_zone_neighbours), sorted(expected_new_neighbours)
        )

        self.assertEqual(
            len(self.original_countries_list) - 1, self.gm.number_of_nodes()
        )

    def test_zona_de_pas_ok(self):
        z1 = 'Besnac'
        z2 = 'Loweh'
        expected = {'Miland'}

        zones = zones_de_pas(self.gm, z1, z2)
        self.assertEqual(expected, zones)

    def test_zona_de_pas_empty(self):
        z1 = 'Ashari'
        z2 = 'Miland'
        expected = set()

        zones = zones_de_pas(self.gm, z1, z2)

        self.assertEqual(expected, zones)

    def test_zona_de_pas_impossible(self):
        z1 = 'Krko'
        z2 = 'Filite'
        expected = {'IMPOSSIBLE'}

        zones = zones_de_pas(self.gm, z1, z2)

        self.assertEqual(expected, zones)
