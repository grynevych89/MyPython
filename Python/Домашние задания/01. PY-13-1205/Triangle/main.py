# 1 - Вводим длины сторон треугольника:
print('Введите длины сторон треугольника:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

# 2 - Вычисляем площадь:
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

# 3 - Выводим результат:
print(f'Площадь треугольника: s = {round(s, 2)}')
