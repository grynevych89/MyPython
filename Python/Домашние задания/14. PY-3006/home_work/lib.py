def display_dep_list(sections) -> None:
    i = 0
    for dep in sections:
        i += 1
        print(f'{i}. {dep}')


def display_emp_list(sections, catalog) -> None:
    if catalog not in sections:
        print('Такой каталог не существует')
    else:
        dep = sections[catalog]
        j = 0
        for emp in dep:
            j += 1
            print(f'{j}. {emp}')


def display_emp_info(sections, catalog, items) -> None:
    if catalog not in sections:
        print('Такой каталог не существует')
    else:
        dep = sections[catalog]
        if items not in dep:
            print('Такого товара не существует')
        else:
            emp = dep[items]
            art = emp['art']
            material = emp['material']
            my_color = emp['my_color']
            cost = emp['cost']
            print(f'Артикул: {art}, Материал: {material}, Цвет: {my_color}, Цена: {cost}')
