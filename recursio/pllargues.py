def recu_pllargues(ls, lmin, accumulator, index=0):
    if index == len(ls):
        return accumulator
    if len(ls[index]) > lmin:
        accumulator.append((ls[index], index))
    index += 1
    return recu_pllargues(ls, lmin, accumulator, index)
def pllargues(ls, lmin):
    return recu_pllargues(ls, lmin, accumulator=[])