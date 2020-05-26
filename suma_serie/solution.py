def suma_serie(x, eps):

    i = 0
    suma = 1

    while True:
        i += 1
        term = (-1)**i * (x**(2 * i))
        if abs(term) < eps:
            return suma
        suma += term
