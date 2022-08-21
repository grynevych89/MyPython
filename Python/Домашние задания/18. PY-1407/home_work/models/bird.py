from models.animals import Animals


class Bird(Animals):

    def __init__(self, name: str, type_animal: str, kingdom: str, type_a: str, detachment: str,
                 family: str, genus: str, view: str, subspecies: str, sniper: str):
        super().__init__(name, type_animal, kingdom, type_a, detachment, family, genus, view, subspecies)
        self._sniper = sniper

    def __str__(self) -> str:
        return super().__str__() + f'\n Особые навыки: {self._sniper}'
