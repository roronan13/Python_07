from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> None:
        pass

    @abstractmethod
    def create_evolved() -> None:
        pass


class FlameFactory(CreatureFactory):
    def create_base():
        pass

    def create_evolved():
        pass


class AquaFactory(CreatureFactory):
    def create_base():
        pass

    def create_evolved():
        pass
