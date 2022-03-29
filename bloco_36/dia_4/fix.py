class Conjunto:
    def __init__(self):
        self.data = [False for _ in range(1001)]

    def add(self, item):
        if 0 <= item <= 1000:
            print(f'Adding {item}')
            self.data[item] = True
        else:
            print(f'Not possible to add {item}')

    def __str__(self):
        string = '{'

        for index, element in enumerate(self.data):
            if element is True:
                string += f'{index}, '

        if len(string) > 1:
            return string[:len(string) - 2] + '}'
        return '{}'

    def __contains__(self, item):
        if 0 <= item <= 1000:
            return self.data[item]
        return False

    def union(self, conjuntoB):
        conjuntoC = Conjunto()
        conjuntoC.data = self.data
        for indexB, itemB in enumerate(conjuntoB.data):
            if itemB is True:
                conjuntoC.data[indexB] = True
        return conjuntoC

    def intersection(self, conjuntoB):
        conjuntoC = Conjunto()
        for indexB, itemB in enumerate(conjuntoB.data):
            if itemB is True and self.data[indexB] is True:
                conjuntoC.data[indexB] = True
        return conjuntoC


if __name__ == '__main__':
    # values = [0, 10, 100, 1000]
    # conjunto = Conjunto()
    # for value in values:
    #     conjunto.add(value)
    # print(conjunto)
    # print(100 in conjunto)
    # print(101 in conjunto)

    conjuntoA = Conjunto()
    for value in [num for num in range(1, 4)]:
        conjuntoA.add(value)

    conjuntoB = Conjunto()
    for value in [num for num in range(4, 6)]:
        conjuntoB.add(value)

    print(conjuntoA.intersection(conjuntoB))
