from abc import ABC, abstractmethod


class Geometric(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Square(Geometric):
    def __init__(self, side):
        self._side = side

    def area(self):
        return self._side ** 2

    def perimeter(self):
        return self._side * 4


class Retangule(Geometric):
    def __init__(self, base, height):
        self._base = base
        self._height = height

    def area(self):
        return self._base * self._height

    def perimeter(self):
        return self._base * 2 + self._height * 2


class Circle(Geometric):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * (self._radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self._radius
