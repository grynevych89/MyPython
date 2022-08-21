from lib import timer


@timer
def bubble_sort(sorted_list: list) -> None:
    """ Пузырьковая сортировка списков """
    n = len(sorted_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sorted_list[j] > sorted_list[j + 1]:
                buff = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = buff


@timer
def selection_sort(_list: list) -> None:
    """Сортировка выбором"""
    n = len(_list)
    for i in range(n - 1):  # n = 5 -> range(6)
        # 1. Находим наименьшее число среди оставшихся:
        m = _list[i]
        k = i
        for j in range(i + 1, n):  # range(0, 6) => 0..5
            if _list[j] < m:
                m = _list[j]
                k = j

        # 2. Переставляем найденное число в начало диапазона:
        buff = _list[i]
        _list[i] = _list[k]
        _list[k] = buff


@timer
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
