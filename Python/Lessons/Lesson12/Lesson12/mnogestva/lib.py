def example1() -> None:
    """Создание множеств"""
    s1 = {10, 20, 20, 40, 30, 30, 40, 50}
    print(s1)
    s2 = set([i for i in range(10, 21)])
    print(s2)
    s3 = set()
    s3.add(100)
    s3.add(200)
    s3.add(300)
    print(s3)


def example2() -> None:
    """Удаление єлементов множеств"""
    s = set([i for i in range(40, 50)])
    print(s)
    s.remove(47)
    s.remove(43)
    if 77 in s:
        s.remove(77)

    s.discard(41)
    s.discard(46)
    s.discard(77)
    print(s)


def example3() -> None:
    """Перебор єлементов множества"""
    s = set()
    for k in range(12):
        s.add(k ** 2)
    print(s)

    for elem in s:
        print(elem)


def example4() -> None:
    """Операции над множествами"""
    # 1 - Копирование:
    s = {111, 222, 333}
    print(s)
    d = s.copy()
    print(d)

    # 2 - Объединение:
    s1 = {10, 20, 30}
    s2 = {70, 80, 90}
    s3 = s1.union(s2)
    s4 = s2.union(s1)
    print(s3)
    print(s4)

    # 3 - Пересечение:
    a1 = {10, 20, 30, 40, 50}
    a2 = {30, 40, 50, 60, 70}
    p1 = a1.intersection(a2)
    p2 = a2.intersection(a1)
    print(p1)
    print(p2)
    print(s1.intersection(s2))

    # 4 - Разность:
    d1 = a1.difference(a2)
    d2 = a2.difference(a1)
    print(d1)
    print(d2)

    # 5 - Семетричная разность:
    sd1 = a1.symmetric_difference(a2)
    print(sd1)
    sd2 = d1.symmetric_difference(d2)
    print(sd2)

    # 6 - Подмножества:
    pm1 = {1000, 2000, 3000, 4000}
    pm2 = {1000, 2000}
    res1 = pm1.issuperset(pm2)
    res2 = pm2.issubset(pm1)
    print(res1)
    print(res2)

    # 7 - Неизменяемые множества:
    students = frozenset({'Tom', 'Bob', 'Alice'})
    print(students)
    happy_students = set(students)
    print(happy_students)
