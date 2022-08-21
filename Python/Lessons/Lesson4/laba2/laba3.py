print('Введите границы диапазона:')
a = int(input('a = '))
b = int(input('b = '))

k = a  # - переменная цикла
while k <= b:
    if k % 2 == 0:
        print(k, end=' ')
    k += 1
