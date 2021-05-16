def get_sanefa(n, d, accumulated_sheeps, white_sheeps=0):
    if len(accumulated_sheeps) == n:
        return accumulated_sheeps

    if white_sheeps == d:
        accumulated_sheeps.append(0)
        return get_sanefa(n, d, accumulated_sheeps)

    accumulated_sheeps.append(1)
    return get_sanefa(n, d, accumulated_sheeps, white_sheeps + 1)


def sanefa(n, d):
    current_list = [0]
    return get_sanefa(n, d, current_list)