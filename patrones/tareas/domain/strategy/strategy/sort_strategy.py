from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

# Definimos la estrategia de ordenación.
