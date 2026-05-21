from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1 import capabilities


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> str:
        return ("No action available")

    @abstractmethod
    def is_valid(self) -> bool:
        return False


class NormalStrategy(BattleStrategy):
    def act(self) -> str:
        print(self.attack())

    def is_valid(self) -> bool:
        return (isinstance(self, Creature))


class AggressiveStrategy(BattleStrategy):
    def act(self) -> str:
        print(self.transform())
        print(self.attack())
        print(self.revert())

    def is_valid(self) -> bool:
        return (isinstance(self, capabilities.TransformCapability))


class DefensiveStrategy(BattleStrategy):
    def act(self) -> str:
        print(self.attack())
        print(self.heal())

    def is_valid(self) -> bool:
        return (isinstance(self, capabilities.HealCapability))


