print('Введите границы диапазона:')
a = int(input('a = '))
b = int(input('b = '))
s = 0
n = 0

for k in range(a, b + 1):
    s += k
    n += 1
print(f'Сумма чисел диапазона: s = {s}')
print(f'Среднее арифметическое: aver = {s / n}')

