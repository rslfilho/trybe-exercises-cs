names_list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def largest_name(names):
    largest = names[0]
    for name in names:
        if len(name) > len(largest):
            largest = name

    return largest


print(largest_name(names_list))
