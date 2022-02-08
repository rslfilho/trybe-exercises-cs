import math


wall_size = 90


def get_necessary_ink(zise):
    ink_liters = zise / 3
    cans = math.ceil(ink_liters / 18)
    total_price = cans * 80

    return cans, total_price


print(get_necessary_ink(wall_size))
