import json


def load_data() -> dict:
    with open('iron_items.json', 'r', encoding='utf-8') as file:
        company = json.load(file)
        print('Данные успешно загружены')
    return company


def save_data(company) -> None:
    with open('iron_items.json', 'w', encoding='utf-8') as file:
        json.dump(company, file)
    print('Данные успешно сохранены')
