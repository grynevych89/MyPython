from lib.base_examples import *
from lib.hoar import *


if __name__ == '__main__':

    # # 1
    # try:
    #     n = int(input('Введите натуральное число < 100: '))
    #     f = factorial(n)
    #     print(f'Результат: {n}! = {f}')
    # except RecursionError:
    #     print('Вы ввели значение за пределами разрешенного диапазона: 1 < n < 100')
    # except ValueError:
    #     print('Вы ввели значение не целого или не числового формата')
    #
    # # 2
    # try:
    #     a = float(input('Введите основание степени: '))
    #     n = int(input('Введите показатель степени (натуральное число): '))
    #     p = power(a, n)
    #     print(f'Результат: {a} ^ {n} = {p}')
    # except RecursionError:
    #     print('Превышена допустимая глубина рекурсии')
    # except ValueError:
    #     print('Вы ввели значение не целого или не числового формата')

    # # 3
    # try:
    #     n = int(input('Введите номер элемента ряда Фибоначи: '))
    #     x = fibo(n)
    #     print(f'Результат: fibo[{n}] = {x}')
    #
    #     for k in range(1, n + 1):
    #         print(fibo(k))
    #
    # except RecursionError:
    #     print('Превышена допустимая глубина рекурсии')
    # except ValueError:
    #     print('Вы ввели значение не целого или не числового формата')

    # 3
    try:
        n = int(input('Введите номер элемента ряда Фибоначи: '))
        x = fibo(n)
        print(f'Результат: fibo[{n}] = {x}')

        for k in range(1, n + 1):
            print(fibo(k))

    except RecursionError:
        print('Превышена допустимая глубина рекурсии')
    except ValueError:
        print('Вы ввели значение не целого или не числового формата')