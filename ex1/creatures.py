from abc import ABC, abstractmethod
from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip !")


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance !")


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        return (f"{self.name} attacks normally !")


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        return (f"{self.name} attacks normally !")
