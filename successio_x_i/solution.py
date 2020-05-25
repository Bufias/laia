def successio(n, epsilon):

    i = 1
    while True:

        calculated = ((i + 3)**2 - 9) / ((i + 3)**3 + i)

        if abs(n - calculated) <= epsilon:
            break

        i += 1

    return i - 1
    # I guess this is because term 0 is when i = 1, term 1 is i = 2...
