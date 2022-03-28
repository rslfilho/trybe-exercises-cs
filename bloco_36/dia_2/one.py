def max_without_instability(array):
    max_online_time = 0
    actual_online_time = 0

    for value in array:
        if value == 1:
            actual_online_time += 1
        else:
            actual_online_time = 0

        if actual_online_time >= max_online_time:
            max_online_time = actual_online_time

    return max_online_time


print(max_without_instability([1, 1, 1, 1, 0, 0, 1, 1]))
