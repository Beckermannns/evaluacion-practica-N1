from abc import ABC, abstractmethod

# Se crea una clase abstracta para las tareas, que define la interfaz común para todas las tareas.
# Esta clase no se puede instanciar directamente y debe ser heredada por otras clases concretas.


class Tarea(ABC):  # Clase base para las tareas
    def __init__(self, titulo, descripcion, estado, tipo):  # Definimos sus atributos
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.tipo = tipo

        @abstractmethod
        def mostrar_info(self):
            return f"Tarea: {self.titulo}, Descripción: {self.descripcion}, Estado: {self.estado}"


class TareaNormal(Tarea):  # Clase que hereda de Tarea
    def mostrar_info(self):
        return f"Tarea Normal - {self.titulo}"


class TareaUrgente(Tarea):  # Clase que hereda de Tarea
    def mostrar_info(self):
        return f"Tarea Urgente - {self.titulo}"


class TareaProgramada(Tarea):  # Clase que hereda de Tarea
    def mostrar_info(self):
        return f"Tarea Programada - {self.titulo}"
