from random import randint
from lib.algo import *


@timer
def selection_sort(_list: list) -> None:
    n = len(_list)
    for i in range(n - 1):
        m = _list[i]
        k = i
        for j in range(i + 1, n):
            if _list[j] < m:
                m = _list[j]
                k = j

        buff = _list[i]
        _list[i] = _list[k]
        _list[k] = buff
