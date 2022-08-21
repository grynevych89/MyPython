def create_dict() -> dict:
    return {
        'Украина': 'Киев',
        'Австралия': 'Канберра',
        'Египет': 'Каир',
        'Канада': 'Оттава',
        'Латвия ': 'Рига'
    }


def capital(words: dict, eng: str) -> str:
    if eng in words:
        return words[eng]
    else:
        return f'Данная страна "{eng}" отсутствует в словаре,' \
               f' или вы ввели не верное название!'
