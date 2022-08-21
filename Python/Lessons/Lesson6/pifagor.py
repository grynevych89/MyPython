print('Таблица пифагора')

# Цикл по строкам:
for i in range(1, 10):
    # Цикл по числам в каждой строке:
    for j in range(1, 10):
        print(f'{(i * j):3d}', end='')
    print()
