from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1 import capabilities


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        print("No action available")
        return

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        return False


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, Creature))


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        try:
            print(creature.transform())
        except Exception as e:
            print(f"{e} (This creature can't transform ..\n)")
            return
        print(creature.attack())
        try:
            print(creature.revert())
        except Exception as e:
            print(f"{e} (This creature can't revert ..\n)")
            return

    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, capabilities.TransformCapability))


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())
        try:
            print(creature.heal())
        except Exception as e:
            print(f"{e} (This creature can't heal ..\n)")
            return

    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, capabilities.HealCapability))
