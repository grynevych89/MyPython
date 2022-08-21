print('Введите границы диапазона:')
a = int(input('a = '))
b = int(input('b = '))

k = a  # - переменная цикла
while k <= b:
    print(k, end=' ')
    k += 1
