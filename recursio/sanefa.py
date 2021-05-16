def get_sanefa(n, d, current_list, white_sheeps=0):
    if len(current_list) == n:
        return current_list

    if white_sheeps == d:
        current_list.append(0)
        return get_sanefa(n, d, current_list)
    else:
        current_list.append(1)
        return get_sanefa(n, d, current_list, white_sheeps + 1)


def sanefa(n, d):
    current_list = [0]
    return get_sanefa(n, d, current_list)