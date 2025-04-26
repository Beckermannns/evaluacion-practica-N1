# Importamos la clase Tarea para asegurar que la clase TareaDecorator herede de ella.
from patrones.tareas.domain.entities.tarea import Tarea
# Se importa la clase ABC y abstractmethod de la biblioteca abc para asegurar que no sean instanciados directamente.
from abc import ABC, abstractmethod

# # Se define una clase abstracta TareaDecorator que hereda de Tarea y ABC.
# # Esta clase se utiliza para agregar funcionalidad adicional a las tareas existentes sin modificar su estructura original.


class TareaDecorator(Tarea, ABC):
    def __init__(self, tarea):
        super().__init__(tarea.titulo, tarea.descripcion, tarea.estado, tarea.tipo)
        # Almacena la tarea original como un atributo privado. Aplicamos encapsulamiento para proteger el atributo _tarea.
        self._tarea = tarea

    # Método abstracto que se implementará en las subclases.

    @abstractmethod
    def mostrar_info(self):
        return self._tarea.mostrar_info()

    # Método que permite acceder a la tarea original a través del decorador y agrega un archivo adjunto.


class TareaConAdjunto(TareaDecorator):
    def __init__(self, tarea, archivo):
        super().__init__(tarea)
        self.archivo = archivo

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Con archivo adjunto: {self.archivo}"

    # Método que permite acceder a la tarea original a través del decorador y agrega el grado de Importante a la tarea base.


class TareaImportante(TareaDecorator):
    def __init__(self, tarea):
        super().__init__(tarea)

    def mostrar_info(self):
        return f"{super().mostrar_info()} - ¡Importante!"

    # Método que permite acceder a la tarea original a través del decorador y agrega el responsable a la tarea base.


class TareaResponsable(TareaDecorator):
    def __init__(self, tarea, responsable):
        super().__init__(tarea)
        self.responsable = responsable

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Responsable: {self.responsable}"
