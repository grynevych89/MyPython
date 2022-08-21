# 1 - Вводим три целых числа:
print('Введите три целых числа:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

# 2 - Выполняем вычисления:
res1 = a + b + c
res2 = a * b * c
res3 = res1 / 3

# 3 - Выводим ответы:
print(f'{a}+{b}+{c}={res1}')
print(f'{a}*{b}*{c}={res2}')
print(f'({a}*{b}*{c})/3={round(res3, 3)}')

