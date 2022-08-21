from models.animals import Animals


class Cats(Animals):

    def __init__(self, name: str, type_animal: str, kingdom: str, type_a: str, detachment: str,
                 family: str, genus: str, view: str, subspecies: str, infra_class: str, lat_name: str):
        super().__init__(name, type_animal, kingdom, type_a, detachment, family, genus, view, subspecies)
        self._infra_class = infra_class
        self._lat_name = lat_name

    def __str__(self) -> str:
        return super().__str__() + f'\n Инфракласс: {self._infra_class} \n Латинское название: {self._lat_name}'
