a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

func = input('Введите нужное действие (+, -, *, =): ')

choice1 = '+'
choice2 = '-'
choice3 = '*'
choice4 = '/'

if func == '+':
    print(a + b)
elif func == '-':
    print(a - b)
elif func == '*':
    print(a * b)
else:
    if func == '/':
        print(int(a / b))
