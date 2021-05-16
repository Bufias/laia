def suma_recursiva(x, accumulator=0, index=0):
    if len(x) == 0:
        return accumulator

    if isinstance(x, int):
        return suma_recursiva(x, accumulator, index + 1)

    if isinstance(x[index], int):
        return suma_recursiva(x, accumulator + x[index], index + 1)

    return suma_recursiva(x, accumulator, index)


def suma_EOL(x):
    return suma_recursiva(x)