def example1() -> None:
    """Создание кортежей"""
    bank_account = ('Василий Пупкий', 100000023456789, 'qwerty1234')
    print(bank_account)
    protected_phone = ('111-11-11',)
    print(protected_phone)
    print(protected_phone[0])


def example2() -> None:
    """Преобразование списка в кортеж"""
    students_list = ['Василий', 'Мария', 'Эдуард']
    print(students_list)
    protected_group = tuple(students_list)
    print(protected_group)


def example3() -> None:
    """Распаковка кортежей"""
    user_info = ('Tom', 25, False)
    name, age, is_married = user_info
    print(f'Имя Пользователя: {name}')
    print(f'Возраст Пользователя: {age}')
    print(f'Семейное положение: {is_married}')


def example4() -> tuple:
    """Возврат множества значений из функции"""
    import random
    numbers = [random.randint(10, 99) for i in range(12)]
    _min = min(numbers)
    _max = max(numbers)
    _sum = sum(numbers)
    return _min, _max, _sum


def example5() -> None:
    """Переборка кортежей"""
    t = (10, 20, 30, 40, 50)
    for index in range(len(t)):
        print(t[index], end=' ')
    print()

    for elem in t:
        print(elem, end=' ')
    print()

    i = 0
    while i < len(t):
        print(t[i], end=' ')
        i += 1


