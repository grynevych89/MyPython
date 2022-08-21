from random import randint


def append_demo():
    print('\n> Добавление элемента в конец списка')
    a = [10, 20, 30, 40, 50]
    print(' ', a)
    x = int(input('  Введите число для добавления в список: '))
    a.append(x)
    print(' ', a)


def insert_demo():
    print('\n> Вставка элемента в список')
    a = [10, 20, 30, 40, 50]
    print(' ', a)
    x = int(input('  Введите число для вставки в список: '))
    k = int(input('  Введите индекс вставляемого элемента: '))
    a.insert(k, x)
    print(' ', a)
    print(f' index = {a.index(x)}')


def remove_demo():
    print('\n> Удаление элемента из списока')
    a = [10, 20, 30, 40, 50]
    print(' ', a)
    x = int(input('  Введите число для удаления списока: '))
    if x in a:
        a.remove(x)
    else:
        print('  Число не входит в список')
    print(' ', a)


def pop_demo():
    print('\n> Удаление элемента из списока')
    a = [10, 20, 30, 40, 50]
    print(' ', a)
    i = int(input('  Введите индекс числа для удаления его из списока: '))
    if i in range(0, len(a)):
        a.pop(i)
    else:
        print(f'  Такой индекс не существует!')
    print(' ', a)


def del_demo():
    print('\n> Удаление элементов из списка оператором "del"')
    a = [10, 20, 30, 40, 50]
    print(' ', a)
    i = int(input('  Введите 1 индекс диапазона: '))
    j = int(input('  Введите 2 индекс диапазона: '))
    n = len(a)
    if i in range(n) and j in range(n + 1) and i < j:
        del a[i:j]
    else:
        print(f'  Something wrong!!!')
    print(' ', a)


def count_demo():
    print('\n> Подсчет кол-ва одинаковых элементов')
    a = [10, 20, 30, 40, 50, 20, 30, 30, 40, 40, 40]
    print(' ', a)
    x = int(input('  Введите число для подсчета: '))
    if x in a:
        k = a.count(x)
        print(f'  Число {x} встречается в списке {k} раза')
    else:
        print(f'  Число {x} не входит в список')


def sort_demo():
    print('\n> Сортировка списков "sort"')
    random_list = [randint(10, 99) for k in range(12)]
    print(random_list)
    random_list.sort()
    print(random_list)


def reverse_demo():
    print('\n> Переворачивание списка "reverse"')
    random_list = [randint(10, 99) for k in range(12)]
    print(random_list)
    random_list.reverse()
    print(random_list)


def slice_demo():
    print('\n> Срезы - копирование части списка "slice"')
    a = [100, 200, 300, 400, 500]
    print(a)
    b = a[1:-1]
    print(b)
    c = a[:-1]
    print(c)
    d = a[1:]
    print(d)
