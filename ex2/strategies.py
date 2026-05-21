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
        try:
            print(self.transform())
        except Exception as e:
            print(f"{e} (This creature can't transform ..\n)")
            return
        print(self.attack())
        try:
            print(self.revert())
        except Exception as e:
            print(f"{e} (This creature can't revert ..\n)")
            return

    def is_valid(self) -> bool:
        return (isinstance(self, capabilities.TransformCapability))


class DefensiveStrategy(BattleStrategy):
    def act(self) -> str:
        print(self.attack())
        try:
            print(self.heal())
        except Exception as e:
            print(f"{e} (This creature can't heal ..\n)")

    def is_valid(self) -> bool:
        return (isinstance(self, capabilities.HealCapability))
