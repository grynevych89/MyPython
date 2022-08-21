from lib.algo import *


def partition(array, left, right):
    m = array[(left + right) // 2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while array[i] < m:
            i += 1
        j -= 1
        while array[j] > m:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


@timer
def quick_sort(nums):
    def _quick_sort(array, left, right):
        if left < right:
            split_index = partition(array, left, right)
            _quick_sort(array, left, split_index)
            _quick_sort(array, split_index + 1, right)

    _quick_sort(nums, 0, len(nums) - 1)
