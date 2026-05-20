from abc import ABC, abstractmethod
import creatures


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> None:
        pass

    @abstractmethod
    def create_evolved() -> None:
        pass


class FlameFactory(CreatureFactory):
    def create_base():
        return (creatures.Flameling())

    def create_evolved():
        return (creatures.Pyrodon())


class AquaFactory(CreatureFactory):
    def create_base():
        return (creatures.Aquabub())

    def create_evolved():
        return (creatures.Torragon())
