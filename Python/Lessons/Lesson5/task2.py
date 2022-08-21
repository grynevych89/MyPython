print('Введите границы диапазона:')
a = int(input('a = '))
b = int(input('b = '))
k = a  # - Переменная цикла!
count = 0
while k <= b:
    if k % 3 == 0:
        print(k)
        count += 1
    k += 1

print(f'Кол-во чисел, кратных 3: {count}')
