def suma_succ(n):

    anterior = 2
    i = 1
    suma = 2

    while True:
        i += 1
        factor = int(i/2)
        if i % 2 == 0:
            terme = anterior + factor
        else:
            terme = anterior * factor

        if terme >= n:
            return suma

        anterior = terme
        suma += anterior
