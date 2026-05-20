from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> None:
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Flameling())

    def create_evolved(self) -> Creature:
        return (Pyrodon())


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Aquabub())

    def create_evolved(self) -> Creature:
        return (Torragon())
