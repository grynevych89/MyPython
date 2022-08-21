def create_dict() -> dict:
    return {
        'girl': 'девочка',
        'boy': 'мальчик',
        'tree': 'дерево',
        'sky': 'небо',
        'street': 'улица'
    }


def translate(words: dict, eng: str) -> str:
    if eng in words:
        return words[eng]
    else:
        return f'Слово {eng} отсутствует в словаре'


def add_word(words: dict, word: str, trans: str) -> str:
    if word in words:
        print('Такое слово уже есть в словаре')
    else:
        words[word] = trans
        return words[word]
