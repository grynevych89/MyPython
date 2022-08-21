class Vector(object):

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __str__(self):
        return f'({self._x}; {self._y})'

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return Vector(x, y)