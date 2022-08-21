from random import randint

n = int(input('Введите размер списка: '))
a = 1
b = 100

random_numbers = [randint(a, b) for i in range(n)]
print(random_numbers)

s1 = 0
s2 = 0

k1 = 0
k2 = 0

for number in random_numbers:
    if number < 50:
        s1 += number
        k1 += 1
    else:
        s2 += number
        k2 += 1

aver1 = round(s1 / k1, 3)
aver2 = round(s2 / k2, 3)

print(f'Среднее арифметическое значение < 50: {aver1}')
print(f'Среднее арифметическое значение >= 50: {aver2}')
