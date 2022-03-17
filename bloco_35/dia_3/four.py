from random import shuffle
from cronometro import Cronometro
from merge import merge_sort
from bubble import bubble_sort


grandeza = 10000
ordenados = list(range(grandeza))
# inversamente_ordenados = list(reversed(range(grandeza)))
aleatorios = ordenados[:]
shuffle(aleatorios)


with Cronometro('Merge'):
    merge_sort(aleatorios)


with Cronometro('Bubble'):
    bubble_sort(aleatorios)
