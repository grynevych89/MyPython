width = int(input('Введите длину стороны квадрата: '))
height = width

for i in range(height):
    if not i or i == height - 1:
        print('*' * width, end='')
        print()
    else:
        print('*' + ' ' * (width - 2) + '*')
