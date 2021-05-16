def recursio_suma(l, accumulator=0, index=0):
    if index == len(l):
        return accumulator
    else:
        accumulator += l[index]
        return recursio_suma(l, accumulator, index + 1)

def suma_llista(l):
    return recursio_suma(l)