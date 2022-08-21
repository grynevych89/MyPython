from vector import Vector
from fraction import Fraction


if __name__ == '__main__':
    # 1
    a = Vector(15.37, 28.99)
    b = Vector(35.02, 17.62)
    c = a + b

    print(a)
    print('+')
    print(b)
    print('=')
    print(c)

    print(f'scalar = {a * b}\n')

    # 2
    f1 = Fraction(5, 8)
    f2 = Fraction(5, 12)
    f3 = f1 + f2
    f3.reduce_fraction()

    print(f1)
    print('+')
    print(f2)
    print('=')
    print(f3)

    #
    z = Fraction(18, 42)
    print()
    print(z)
    n = z.nod()
    z.reduce_fraction()
    print(z)
