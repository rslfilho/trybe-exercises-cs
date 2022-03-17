def how_many_even(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + how_many_even(n - 1)
    else:
        return how_many_even(n - 1)


print(how_many_even(9))
