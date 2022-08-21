class Animals(object):

    def __init__(self, name: str, class_animal: str, kingdom: str, type_a: str, detachment: str, family: str,
                 genus: str, view: str, subspecies: str):
        self._name = name
        self._class_animal = class_animal
        self._kingdom = kingdom
        self._type = type_a
        self._detachment = detachment
        self._family = family
        self._genus = genus
        self._view = view
        self._subspecies = subspecies
        self._animals = []

    def __str__(self) -> str:
        return f'\n> Животное: \n Название: {self._name} \n Класс: {self._class_animal} \n Царство: {self._kingdom}' \
               f'\n Тип: {self._type} \n Отряд: {self._detachment} \n Семейство: {self._family} \n Род: {self._genus}' \
               f'\n Вид: {self._view} \n Подвид: {self._subspecies}'
