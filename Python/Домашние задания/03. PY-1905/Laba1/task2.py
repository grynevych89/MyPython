from math import sqrt

# 1 - Вводим координаты 1-ой точки:
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

# 2 - Вводим координаты 2-ой точки:
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

# 3 - Вычисляем расстояние между точками:
dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 4 - Выводим результат:
print(f'Расстояние между точками: {round(dist, 3)}')