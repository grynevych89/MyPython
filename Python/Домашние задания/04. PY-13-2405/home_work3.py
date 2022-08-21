print('Введите границы диапазона:')
a = int(input('a = '))
b = int(input('b = '))

num = a

for num in range(a, b):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=' ')
    elif num % 3 == 0:
        print("Fizz", end=' ')
    elif num % 5 == 0:
        print("Buzz", end=' ')
    else:
        print(num, end=' ')
