from abc import ABC, abstractmethod


class StrategyInterface(ABC):
    @classmethod
    @abstractmethod
    def next_index(self):
        raise NotImplementedError


class RegularStrategy(StrategyInterface):
    initial_page = 0

    @classmethod
    def next_index(cls, index):
        return index + 1


class ReverseStrategy(StrategyInterface):
    initial_page = -1

    @classmethod
    def next_index(cls, index):
        return index - 1


class BaralhoIterator:
    def __init__(self, cartas, strategy):
        self.strategy = strategy
        self._cartas = cartas
        self._current_page = strategy.initial_page

    def __next__(self):
        try:
            carta = self._cartas[self._current_page]
        except IndexError:
            raise StopIteration()
        else:
            self._current_page = self.strategy.next_index(self._current_page)
            return carta


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f'<{self.valor} de {self.naipe}>'


class Baralho:
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self, strategy):
        self.strategy = strategy
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return BaralhoIterator(self._cartas, self.strategy)


baralho_normal = Baralho(ReverseStrategy)

for carta in baralho_normal:
    print(carta)
