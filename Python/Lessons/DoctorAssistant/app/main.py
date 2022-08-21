from models.hospital import Hospital
from models.doctor import Doctor
from repos.hospitals import Hospitals
from repos.doctors import Doctors

if __name__ == '__main__':
    # try:
    #     data_manager1 = Hospitals(Hospital())
    #     data_manager1.display_all_hospitals()
    # except RuntimeError as rte:
    #     print(rte)

    try:
        data_manager2 = Doctors(Doctor())
        data_manager2.add_doctor_dialog()
        data_manager2.display_all_doctors()
    except RuntimeError as rte:
        print(rte)
