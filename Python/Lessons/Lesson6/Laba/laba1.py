try:
    a = int(input('Введите число от 1 до 10: '))
    if a < 1 or a > 10:
        raise RuntimeError('Выход за пределы заданного диапазона значений')
    for i in range(1, 11):
        print(f'{a} x {i} = {a * i}')
except ValueError as err1:
    print(f'Неверный формат ввода! => {err1}')
except RuntimeError as err2:
    print(f'Ошибка ввода => {err2}')
