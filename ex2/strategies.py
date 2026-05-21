from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        return False
    

class 

