class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f'<{self.valor} de {self.naipe}>'


class Baralho:
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return BaralhoIterator(self._cartas)


class BaralhoIterator:
    def __init__(self, cartas):
        self._cartas = cartas
        self._current_page = 0

    def __next__(self):
        try:
            carta = self._cartas[self._current_page]
        except IndexError:
            raise StopIteration()
        else:
            self._current_page += 1
            return carta


baralho = Baralho()

# for carta in baralho:
#     print(carta)
