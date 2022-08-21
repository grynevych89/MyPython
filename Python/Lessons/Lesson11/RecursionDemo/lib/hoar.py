def quick_sort(array, left, right):
    if left >= right:
        return
    else:
        m = array[(left + right) // 2]
        i = left
        j = right

        while i <= j:
            while array[i] < m:
                i += 1
            while array[j] > m:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
                quick_sort(array, left, j)
                quick_sort(array, i, right)
