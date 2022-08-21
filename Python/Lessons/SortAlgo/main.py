from lib import *
from algo import *


if __name__ == '__main__':
    # 1
    a = create_rand_list(10000, 10, 99)
    b1 = a.copy()
    b2 = a.copy()
    b3 = a.copy()

    # 2
    bubble_sort(b1)
    selection_sort(b2)
    insertion_sort(b3)
