def how_many_even(n):
    if n % 2 == 0:
        return round(n / 2)
    else:
        return round((n / 2) - 1)


print(how_many_even(9))
