from models.animals import Animals


class Fish(Animals):

    def __init__(self, name: str, type_animal: str, kingdom: str, type_a: str, detachment: str,
                 family: str, genus: str, view: str, subspecies: str, ultimate: str):
        super().__init__(name, type_animal, kingdom, type_a, detachment, family, genus, view, subspecies)
        self._ultimate = ultimate

    def __str__(self) -> str:
        return super().__str__() + f'\n Способности: {self._ultimate}'
