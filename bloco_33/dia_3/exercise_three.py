from exercise_two import Baralho


class BaralhoInverso(Baralho):
    def __iter__(self):
        return BaralhoReverseIterator(self._cartas)


class BaralhoReverseIterator:
    def __init__(self, cartas):
        self._cartas = cartas
        self._current_page = -1

    def __next__(self):
        try:
            carta = self._cartas[self._current_page]
        except IndexError:
            raise StopIteration()
        else:
            self._current_page -= 1
            return carta


baralho_inverso = BaralhoInverso()


for carta in baralho_inverso:
    print(carta)
