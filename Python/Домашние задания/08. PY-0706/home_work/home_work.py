from random import randint

list1 = ([randint(10, 100) for k in range(12)])  # Первый список
list2 = ([randint(10, 100) for j in range(12)])  # Второй список
list_all = list1 + list2
list_min_max = [min(list1), max(list1), min(list2), max(list2)]

print("\n> Первый список", list1)
print("\n> Второй список", list2)
print("\n> Общий список", list_all)
print("\n> Список уникальных чисел", list(set(list_all)))
print("\n> Список с повторяющимися числами", [x for x in list1 if x in list2])
print("\n> Список чисел без повторения", list(set(list_all)))
print("\n> Мин и макс значения списков", list_min_max)
