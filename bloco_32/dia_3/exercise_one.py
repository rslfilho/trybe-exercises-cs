n = 15


def fizz_buzz(x):
    result = []

    for number in range(1, x + 1):
        if number % 3 == 0 and number % 5 == 0:
            result.append('FizzBuzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
        else:
            result.append(number)

    return result


print(fizz_buzz(n))
