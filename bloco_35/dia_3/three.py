from random import shuffle
from cronometro import Cronometro
from selection import selection_sort
from insertion import insertion_sort


grandeza = 100000
ordenados = list(range(grandeza))
inversamente_ordenados = list(reversed(range(grandeza)))
aleatorios = ordenados[:]
shuffle(aleatorios)


with Cronometro('Execução'):
    # Grandeza 10000
    # insertion_sort(ordenados) # 0.003325057999999999 segundos
    # selection_sort(ordenados) # 8.044019407999999 segundos
    # selection_sort(aleatorios) # 8.114711533 segundos
    # selection_sort(inversamente_ordenados) # 8.231830096 segundos
    # insertion_sort(aleatorios) # 9.269805799 segundos
    # insertion_sort(inversamente_ordenados) # 19.23051404 segundos

    # Grandeza 100
    # insertion_sort(ordenados) # 4.869299999999549e-05 segundos
    # insertion_sort(aleatorios) # 0.0006686249999999991 segundos
    # selection_sort(ordenados) # 0.0006851010000000005 segundos
    # selection_sort(aleatorios) # 0.001038750000000005 segundos
    # selection_sort(inversamente_ordenados) # 0.0011497700000000013 segundos
    # insertion_sort(inversamente_ordenados) # 0.002586682 segundos
