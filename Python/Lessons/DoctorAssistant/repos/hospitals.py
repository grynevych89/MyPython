from models.hospital import Hospital


class Hospitals(object):

    def __init__(self, hospital_model: Hospital):
        self._hospital_model = hospital_model

    def add_hospital_dialog(self) -> None:
        """Консольный диалог добавления поликлиники в базу"""
        print('Введите параметры для добавления в базу нового госпиталя:')
        name = input('Название поликлиники: ')
        phone = input('Телефон регистратуры: ')
        address = input('Адресс поликлиники: ')
        self._hospital_model.add_hospital(name, phone, address)
        print('Поликлиника успешно добавлена в базу')

    def display_all_hospitals(self) -> None:
        """Вывод в консоль списка поликлиник"""
        hospitals_list = self._hospital_model.get_all_hospitals()
        count = 0
        for h in hospitals_list:
            count += 1
            print(f'{count}. {h[1]}')
