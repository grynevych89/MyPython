from lib.base_examples import *
from lib.hoar import quick_sort

if __name__ == '__main__':

    a = create_rand_list(10000, 1, 1000)
    b1 = a.copy()
    b2 = a.copy()

    print('Selection Sort')
    display_list(b1)
    selection_sort(b1)
    display_list(b1)
    print()
    print('Quick Sort')
    display_list(b2)
    quick_sort(b2)
    display_list(b2)
