def students_inside(in_list, out_list, search):
    result = 0

    for index in range(len(in_list)):
        if in_list[index] <= search <= out_list[index]:
            result += 1

    return result


print(students_inside([1, 2, 3], [3, 2, 7], 4))
