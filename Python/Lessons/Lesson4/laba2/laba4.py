print('Введите границы диапазона:')
a = int(input('a = '))
b = int(input('b = '))

k = b  # - переменная цикла
while k >= a:
    print(k, end=' ')
    k -= 1
