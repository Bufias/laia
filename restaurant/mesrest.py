def cerca_taula(r, n):
    for id_taula in range(len(r)):

        ocupacio_rest_inicial = r.ocupacio()

        r[id_taula] = n

        nova_ocupacio_rest = r.ocupacio()

        if ocupacio_rest_inicial != nova_ocupacio_rest:
            return id_taula

    return -1
