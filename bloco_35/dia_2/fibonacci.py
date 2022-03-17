def fibonacci(n):
    array = [0, 1]
    while len(array) < n:
        array.append(array[-1] + array[-2])

    return array[n-1]


def fibonacci2(n):
    if n < 2:
        return n
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)


print(fibonacci(1))  # saída: 0
print(fibonacci(2))  # saída: 1
print(fibonacci(3))  # saída: 1
print(fibonacci(4))  # saída: 2
print(fibonacci(5))  # saída: 3
print(fibonacci(6))  # saída: 5
print(fibonacci(7))  # saída: 8
print(fibonacci(8))  # saída: 13
print(fibonacci(9))  # saída: 21
print(fibonacci(10))  # saída: 34
