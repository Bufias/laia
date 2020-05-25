def suma_serie(x, eps):

    i = 0
    term = 1
    suma = 0
    while abs(term) >= eps:
        suma += term
        i += 1
        term = (-1)**i * (x**(2 * i))

    return suma

