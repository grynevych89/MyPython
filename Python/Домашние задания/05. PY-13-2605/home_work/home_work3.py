"""
Задание 3
Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись «Number is positive»,
если меньше нуля «Number is negative», если равно нулю «Number is equal to zero».
Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»
"""
print('Введите границы диапазона:')
a = int(input('a = '))


if a > 0 and a != 7:
    print('«Number is positive»')
elif a < 0:
    print('«Number is negative»')
elif a == 0:
    print('«Number is equal to zero»')
else:
    print('«Good bye!»')
