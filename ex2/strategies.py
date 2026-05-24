from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1 import capabilities
from typing import cast


class StrategyError(Exception):
    def __init__(self, error_message: str = "Unknown strategy error."):
        super().__init__(error_message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        print("No action available")

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        return False


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, Creature))

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise StrategyError(f"{creature.name} can't attack ..")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        # if isinstance(creature, capabilities.TransformCapability):
        #     return True
        # else:
        #     return False
        return (isinstance(creature, capabilities.TransformCapability))

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            casted_creature = cast(capabilities.TransformCapability, creature)

            print(casted_creature.transform())
            print(creature.attack())
            print(casted_creature.revert())
        else:
            raise StrategyError(f"{creature.name} can't\
transform and revert ..")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, capabilities.HealCapability))

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            casted_creature = cast(capabilities.HealCapability, creature)

            print(creature.attack())
            print(casted_creature.heal())
        else:
            raise StrategyError(f"{creature.name} can't heal ..")
