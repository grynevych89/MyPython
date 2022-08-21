import copy

from data import save_data


def display_dep_list(company) -> None:
    i = 0
    for dep in company:
        i += 1
        print(f'{i}. {dep}')


def display_emp_list(company, dep_name) -> None:
    if dep_name not in company:
        print('Такой отдел не существует')
    else:
        dep = company[dep_name]
        j = 0
        for emp in dep:
            j += 1
            print(f'{j}. {emp}')


def display_emp_info(company, dep_name, emp_name) -> None:
    if dep_name not in company:
        print('Такой отдел не существует')
    else:
        dep = company[dep_name]
        if emp_name not in dep:
            print('Такого сотрудника не существует')
        else:
            emp = dep[emp_name]
            age = emp['age']
            pos = emp['position']
            sal = emp['salary']
            print(f'Возраст: {age}, Должность: {pos}, Зарплата: {sal}')


def search_emp(company, emp_name) -> None:
    success = False
    for dep_name in company.keys():
        dep = company[dep_name]
        if emp_name in dep:
            emp = dep[emp_name]
            print('Сотрудник найден')
            print(f'{dep_name} => {emp_name} - {emp["position"]}')
            success = True
            break
    if not success:
        print(f'Сотрудник {emp_name} не найден')


def check_exists_emp(company, dep_name, emp_name) -> bool:
    if dep_name not in company:
        print(f'{dep_name} - не найден')
        return False
    else:
        dep = company[dep_name]
        if emp_name not in dep:
            print(f'{emp_name} - не найден')
            return False
        else:
            return True


def add_emp(company, dep_name, emp_name, age, position, salary) -> None:
    if dep_name not in company:
        print(f'{dep_name} - не найден')
    else:
        dep = company[dep_name]
        if emp_name in dep:
            print(f'{emp_name} - уже числится в качестве сотрудника. '
                  f'Добавьте идентификатор')
        else:
            dep[emp_name] = {
                'age': age,
                'position': position,
                'salary': salary
            }
            save_data(company)
            print('Сотрудник успешно добавлен')


def del_emp(company, dep_name, emp_name) -> None:
    if check_exists_emp(company, dep_name, emp_name):
        del company[dep_name][emp_name]
        print('Сотрудник успешно удален')


def edit_emp(company, dep_name, emp_name, age, position, salary) -> None:
    if dep_name not in company:
        print(f'{dep_name} - не найден')
    else:
        dep = company[dep_name]
        dep[emp_name] = {
            'age': age,
            'position': position,
            'salary': salary
        }
        dict.update(dep[emp_name])
        print('Изменение сохранено')


def change_dep(company, dep_name, dep_name2, emp_name) -> None:
    if dep_name not in company:
        print(f'{dep_name} - не найден')
    elif not check_exists_emp(company, dep_name, emp_name):
        print(f'{emp_name} - не найден')
    else:
        emp = company[dep_name][emp_name]
        del_emp(company, dep_name, emp_name)
        add_emp(company, dep_name2, emp_name, emp['age'], emp['position'], emp['salary'])
        save_data(company)
