print('Введите границы диапазона:')
a = int(input('a = '))
b = int(input('b = '))

num = a
while num <= b:
    if num % 7 == 0:
        print(num, end=' ')
    num += 1
