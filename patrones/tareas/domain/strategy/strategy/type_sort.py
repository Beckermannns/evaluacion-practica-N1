from patrones.tareas.domain.strategy.strategy.sort_strategy import SortStrategy
from typing import List
from patrones.tareas.domain.entities.tarea import Tarea


class TypeSortStrategy(SortStrategy):
    def sort(self, tareas: List[Tarea]) -> List[Tarea]:
        return sorted(tareas, key=lambda tarea: tarea.tipo)
