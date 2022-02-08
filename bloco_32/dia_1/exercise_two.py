numbers_list = [2, 4, 5, 7, 10, 13, 19, 23]


def average(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum / len(numbers)


print(average(numbers_list))
