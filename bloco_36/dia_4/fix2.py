entrada = [1, 3, 2, 4, 5, 1]
# saída: 1


def find_duplicate(array):
    new_set = set(array)

    for num in array:
        if num in new_set:
            new_set.discard(num)
        else:
            return num


print(find_duplicate(entrada))

# Exercício 07
estudantes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
lista1_entregues = ['a', 'd', 'g', 'c']
lista2_entregues = ['c', 'a', 'f']


def not_list1(students, list1):
    return set(students).difference(set(list1))

# print(not_list1(estudantes, lista1_entregues))


def both_lists(list1, list2):
    return set(list1).intersection(set(list2))

# print(both_lists(lista1_entregues, lista2_entregues))


def some_list(list1, list2):
    return set(list1).union(set(list2))

# print(some_list(lista1_entregues, lista2_entregues))


def any_list(students, list1, list2):
    return set(students).difference(set(list1), set(list2))

# print(any_list(estudantes, lista1_entregues, lista2_entregues))
