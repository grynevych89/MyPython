import json


def load_data() -> dict:
    with open('hrdep.json', 'r', encoding='utf-8') as file:
        company = json.load(file)
        print('Данные успешно загружены')
    return company


def save_data(company) -> None:
    with open('hrdep.json', 'w', encoding='utf-8') as file:
        json.dump(company, file)
    print('Данные успешно сохранены')

