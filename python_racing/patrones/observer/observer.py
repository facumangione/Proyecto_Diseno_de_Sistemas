
from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass