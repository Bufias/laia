from math import factorial


def sinus_aproximat(valor_x, eps):

    i = 0
    previous_accumulated = 0
    while 1:
        param = 2 * i + 1

        if i % 2:
            factor = -1
        else:
            factor = 1
        # if-else structure is the same as (-1)**i

        term = factor * ((valor_x ** param) / factorial(param))

        approx_value = term + previous_accumulated
        previous_accumulated = approx_value
        i += 1

        if abs(term) < eps:
            return approx_value

