def suma_succ(n):

    anterior = 2
    i = 1
    suma = 0

    while anterior < n:
        suma += anterior
        i += 1
        factor = int(i/2)
        if i % 2 == 0:
            terme = anterior + factor
        else:
            terme = anterior * factor

        anterior = terme

    return suma
