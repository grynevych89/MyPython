from data import load_data
from menu import display_menu, get_choice, allow_continue
from lib import display_dep_list, display_emp_list, display_emp_info


if __name__ == '__main__':
    sections = load_data()
    while True:
        display_menu()
        choice = get_choice()
        if choice == 1:
            display_dep_list(sections)
        elif choice == 2:
            catalog = input('Введите название каталога: ')
            display_emp_list(sections, catalog)
        elif choice == 3:
            catalog = input('Введите название каталога: ')
            items = input('Введите название товара: ')
            display_emp_info(sections, catalog, items)
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            pass
        else:
            pass
        if not allow_continue():
            break
