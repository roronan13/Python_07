from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        return ("No heal available")


class TransformCapability(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        return ("No transform available")

    @abstractmethod
    def revert(self) -> str:
        return ("No revert available")
