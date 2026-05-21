from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        return ("No heal available")


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        return ("No transform available")

    @abstractmethod
    def revert(self) -> str:
        return ("No revert available")
