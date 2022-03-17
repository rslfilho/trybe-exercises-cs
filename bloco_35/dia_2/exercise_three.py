def biggest(array):
    if len(array) == 1:
        return array[0]
    elif array[1] > array[0]:
        return biggest(array[1:])
    else:
        array.pop(1)
        return biggest(array)


print(biggest([3, 1, 6, 4, 9, 12, 2, 30]))
