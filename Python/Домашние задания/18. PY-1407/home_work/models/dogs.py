from models.animals import Animals


class Dogs(Animals):

    def __init__(self, name: str, type_animal: str, kingdom: str, type_a: str, detachment: str,
                 family: str, genus: str, view: str, subspecies: str, del_type: str, lat_name: str):
        super().__init__(name, type_animal, kingdom, type_a, detachment, family, genus, view, subspecies)
        self._lat_name = lat_name
        self._del_type = del_type

    def __str__(self) -> str:
        return super().__str__() + f'\n Делятся на породы: {self._del_type} \n Латинское название: {self._lat_name}'
