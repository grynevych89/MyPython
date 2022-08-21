width = int(input('Введите длину стороны прямоугольника: '))
height = int(input('Введите высоту стороны прямоугольника: '))
for i in range(height):
    for j in range(width):
        print('*', end=' ')
    print()
