from patrones.tareas.domain.entities.tarea import TareaNormal, TareaUrgente, TareaProgramada

# Se define una clase de fabrica que se encargara de crear instancias de las tareas.
# Este es mi Factory Method, ya que la clase TareaFactory es responsable de crear instancias de las clases TareaNormal, TareaUrgente y TareaProgramada.


class TareaFactory:
    @staticmethod
    def crear_tarea(titulo, descripcion, estado, tipo):
        tipo = tipo.lower()

        if tipo == "normal":  # Condicional que identifica el tipo de tarea a crear.
            # Si el tipo es normal, crea una instancia de TareaNormal.
            return TareaNormal(titulo, descripcion, estado, tipo)
        if tipo == "urgente":
            # Si el tipo es urgente, crea una instancia de TareaUrgente.
            return TareaUrgente(titulo, descripcion, estado, tipo)
        if tipo == "programada":
            # Si el tipo es programada, crea una instancia de TareaProgramada.
            return TareaProgramada(titulo, descripcion, estado, tipo)
        else:
            raise ValueError(f"Tipo de tarea desconocido: {tipo}")
