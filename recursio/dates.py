def recu_dates(ldates, mes, accumulator, index=0):

    if index == len(ldates):
        return accumulator
    if ldates[index].month == mes:
        accumulator.append(ldates[index].day)
    index += 1
    return recu_dates(ldates, mes, accumulator, index)


def dates(ldates, mes):
    return recu_dates(ldates, mes, accumulator=[])
