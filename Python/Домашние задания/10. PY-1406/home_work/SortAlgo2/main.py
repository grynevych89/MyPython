from lib import *
from algo import *


if __name__ == '__main__':
    # 1
    list1 = create_rand_list(30, 10, 99)
    display_list(list1)
    bubble_sort(list1)

    a = list1[:15]
    b = list1[:14:-1]

    display_list(list1)
    display_list(a + b)
