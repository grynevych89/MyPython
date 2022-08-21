from random import randint


def create_rand_list(size: int, number_min: int, number_max: int) -> list:
    """ Создание рандомного списка """
    return [randint(number_min, number_max) for _ in range(size)]


def display_list(target_list: list) -> None:
    """ Вывод элементов списка на экран консоли """
    for elem in target_list:
        print(elem, end=' ')
    print()


def timer(func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f'Время выполнения: {t2 - t1} секунд')
        return res
    return wrapper


def display(**kwargs):
    for k in kwargs:
        print(k.title())
