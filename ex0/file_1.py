from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        return ("No attack available")

    def describe(self) -> str:
        return (f"creature {self.name} which is type {self.type}")


class Flameling(Creature):
    def __init__(self, name: str, type: str):
        super().__init__(name, type)

    def attack(self) -> str:
        return (f"{self.name} uses Ember !")


class Pyrodon(Creature):
    def __init__(self, name: str, type: str):
        super().__init__(name, type)

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower !")


class Aquabub(Creature):
    def __init__(self, name: str, type: str):
        super().__init__(name, type)

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun !")


class Torragon(Creature):
    def __init__(self, name: str, type: str):
        super().__init__(name, type)

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump !")
