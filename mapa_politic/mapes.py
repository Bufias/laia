import networkx as nx


def fusiona_zones(gm, z1, z2, z3):
    adjacents_z1 = list(gm.adj[z1])
    adjacents_z2 = list(gm.adj[z2])

    if z2 not in adjacents_z1:
        ## It is not possible to join the zones
        return

    adjacents_z1.remove(z2)
    adjacents_z2.remove(z1)
    adjacents_z3 = set(adjacents_z1 + adjacents_z2)

    gm.remove_node(z1)
    gm.remove_node(z2)

    gm.add_node(z3)

    [gm.add_edge(z3, adjacent) for adjacent in adjacents_z3]


def zones_de_pas(gm, z1, z2):
    no_way_path = {'IMPOSSIBLE'}
    all_paths = [set(path) for path in nx.all_simple_paths(gm, z1, z2)]

    if not all_paths:
        return no_way_path

    intersection = set.intersection(*all_paths)
    intersection.remove(z1)
    intersection.remove(z2)

    return intersection
