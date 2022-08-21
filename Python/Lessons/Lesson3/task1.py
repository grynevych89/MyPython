"""
    Найти наибольшее из трех целых чисел
"""

print('Введите 3 целых числа: ')
a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print('Среди чисел, есть одинаковые')
