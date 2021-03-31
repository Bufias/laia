import math
from itertools import groupby
from functools import reduce

def primers():
    b = 7
    anterior = 7
    n = 1
    while True:
        yield b
        n += 1
        seguent = anterior + math.gcd(n, anterior)
        b = seguent - anterior
        anterior = seguent


def sense_uns(it):
    return filter(lambda x: x != 1, it)


def n_uns(it):
    accumulator = 0
    while True:
        try:
            new_number = next(it)
        except StopIteration:
            yield accumulator
            return

        if new_number == 1:
            accumulator += 1
        else:
            if accumulator != 0:
                yield accumulator
                accumulator = 0
