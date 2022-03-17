def binary_search(array, low_index, high_index, value):
    if high_index < low_index:
        raise ValueError(f"{value} is not in list")

    middle_index = (high_index + low_index) // 2

    if array[middle_index] == value:
        return middle_index
    elif array[middle_index] > value:
        return binary_search(array, low_index, middle_index - 1, value)
    else:
        return binary_search(array, middle_index + 1, high_index, value)


def binary_search_iterative(array, target):
    low_index = 0
    high_index = len(array) - 1

    while high_index >= low_index:
        middle_index = (high_index + low_index) // 2
        middle_item = array[middle_index]
        print(middle_item)
        if (middle_item == target):
            return middle_index
        elif middle_item > target:
            high_index = middle_index - 1
        else:
            low_index = middle_index + 1

    raise ValueError('target not found')


array = [2, 3, 4, 10, 40]
target = 40

# result = binary_search(array, 0, len(array) - 1, target)
# print(f"Elemento encontrado na posição: {result}")

# result2 = binary_search_iterative(array, target)
# print(f'Elemento encontrado na posição: {result2}')
