from random import randint

n = int(input('Введите размер списка: '))
a = 0
b = 5

random_numbers = [randint(a, b) for i in range(n)]
print(random_numbers)

s = 0
for number in random_numbers:
    s += number

aver = round(s / n, 3)
print(f'Среднее арифметическое значение: {aver}')

