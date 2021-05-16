def recur_elimina(lnums, n, accumulator, index=0):

    if index == len(lnums):
        return accumulator

    if lnums[index] != n:
        accumulator.append(lnums[index])
    index += 1
    return recur_elimina(lnums, n, accumulator, index)


def elimina(lnums, n):
    return recur_elimina(lnums, n, [])
