class Fraction(object):

    def __init__(self, num: int, den: int):
        self._num = num
        self._den = den
        self._intpart = 0

    def __str__(self):
        self.norm()
        if self._intpart == 0:
            return f'({self._num}/{self._den})'
        elif self._num == 0:
            return str(self._intpart)
        else:
            return f'{self._intpart}({self._num}/{self._den})'

    def __add__(self, other):
        d1 = self._num * other._den
        d2 = other._num * self._den
        d3 = self._den * other._den
        return Fraction(d1 + d2, d3)

    def __sub__(self, other):
        d1 = self._num * other._den
        d2 = other._num * self._den
        d3 = self._den * other._den
        return Fraction(d1 - d2, d3)

    def __mul__(self, other):
        d1 = self._num * other._num
        d2 = self._den * other._den
        return Fraction(d1, d2)

    def __truediv__(self, other):
        d1 = self._num * other._den
        d2 = self._den * other._num
        return Fraction(d1, d2)

    def is_improper(self) -> bool:
        return self._num >= self._den

    def norm(self) -> None:
        if self.is_improper():
            if self._num == self._den:
                self._intpart = 1
                self._num = 0
            else:
                self._intpart = self._num // self._den
                self._num = self._num % self._den

    def nod(self) -> int:
        a = self._num
        b = self._den
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def reduce_fraction(self) -> None:
        n = self.nod()
        self._num //= n
        self._den //= n
