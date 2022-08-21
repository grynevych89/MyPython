from data import load_data
from menu import display_menu, get_choice, allow_continue
from lib1 import display_dep_list, display_emp_list, display_emp_info, \
    search_emp, add_emp, del_emp, edit_emp, change_dep
from os import system


if __name__ == '__main__':
    company = load_data()
    # save_data(company)
    while True:
        display_menu()
        choice = get_choice()
        if choice == 1:
            display_dep_list(company)
        elif choice == 2:
            dep_name = input('Введите название отдела: ')
            display_emp_list(company, dep_name)
        elif choice == 3:
            dep_name = input('Введите имя отдела: ')
            emp_name = input('Введите имя сотрудника: ')
            display_emp_info(company, dep_name, emp_name)
        elif choice == 4:
            emp_name = input('Кого ищем? ')
            search_emp(company, emp_name)
        elif choice == 5:
            dep_name = input('Введите имя отдела: ')
            emp_name = input('Введите имя сотрудника: ')
            age = input('Сколько ему/ей лет? - ')
            position = input('Должность? - ')
            salary = input('Зарплата? - ')
            add_emp(company, dep_name, emp_name, age, position, salary)
        elif choice == 6:
            dep_name = input('Введите имя отдела: ')
            emp_name = input('Введите имя сотрудника: ')
            del_emp(company, dep_name, emp_name)
        elif choice == 7:
            dep_name = input('Введите имя отдела: ')
            emp_name = input('Введите имя сотрудника: ')
            age = input('Сколько ему/ей лет? - ')
            position = input('Должность? - ')
            salary = input('Зарплата? - ')
            edit_emp(company, dep_name, emp_name, age, position, salary)
        elif choice == 8:
            dep_name = input('Введите имя отдела: ')
            emp_name = input('Введите имя сотрудника: ')
            dep_name2 = input('Введите имя нового отдела: ')
            change_dep(company, dep_name, dep_name2, emp_name)
        elif choice == 9:
            break
        else:
            print('Введено не верное значение!')
        if not allow_continue():
            break
    print('Программа завершена')
    system("PAUSE")
