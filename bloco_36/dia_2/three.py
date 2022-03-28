def good_combinations(products):
    result = 0

    for index, product in enumerate(products):
        for index2 in range(index + 1, len(products)):
            if product == products[index2]:
                result += 1

    return result


print(good_combinations([1, 3, 1, 1, 2, 3]))
