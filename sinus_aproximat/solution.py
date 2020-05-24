from math import factorial


def sinus_aproximat(valor_x, eps):

    i = 0
    previous_term = valor_x
    approx_value = valor_x
    while abs(previous_term) >= eps:
        i += 1
        param = 2 * i + 1

        if i % 2:
            factor = -1
        else:
            factor = 1
        # if-else structure is the same as (-1)**i

        new_term = factor * ((valor_x ** param) / factorial(param))

        approx_value += new_term

        previous_term = new_term

    return approx_value
