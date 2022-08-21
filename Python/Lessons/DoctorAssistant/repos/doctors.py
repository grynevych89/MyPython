from models.doctor import Doctor


class Doctors(object):

    def __init__(self, doctor_model: Doctor):
        self._doctor_model = doctor_model

    def add_doctor_dialog(self) -> None:
        """Консольный диалог добавления Доктора в базу"""
        print('Введите параметры для добавления в базу нового Доктора:')
        name = input('ФИО: ')
        phone = input('Телефон: ')
        hospital_id = int(input('ID поликлиники: '))
        self._doctor_model.add_doctor(name, phone, hospital_id)
        print('Доктор успешно добавлен в базу')

    def display_all_doctors(self) -> None:
        """Вывод в консоль списка Докторов"""
        doctors_list = self._doctor_model.get_all_doctors()
        count = 0
        for d in doctors_list:
            count += 1
            print(f'{count}. {d[1]}')
