def reverse(array):
    array.reverse()
    return array


def reverse2(list):
    if len(list) < 2:
        return list
    else:
        return [list[-1]] + reverse2(list[: len(list) - 1])


test = [0, 1, 2, 3, 4, 5]
print(reverse2(test))
