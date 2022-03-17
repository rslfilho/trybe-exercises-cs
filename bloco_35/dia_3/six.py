entrada = [True, True, True, True, False, False, False]
# saída: 4


entrada2 = [True, True, False, False, False, False, False]
# saída: 2


def search(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index

    raise ValueError('target not found')


print(search(entrada2, False))
