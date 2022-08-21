print('Введите границы диапазона:')
a = int(input('a = '))
b = int(input('b = '))

num1 = a
while num1 <= b:
    print(num1, end=' ')
    num1 += 1
print()

num2 = b
while num2 >= a:
    print(num2, end=' ')
    num2 -= 1
print()

num3 = a
while num3 <= b:
    if num3 % 7 == 0:
        print(num3, end=' ')
    num3 += 1
print()

num4 = a
while num4 <= b:
    if num4 % 5 == 0:
        print(num4, end=' ')
    num4 += 1
print()
