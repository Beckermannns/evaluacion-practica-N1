from patrones.tareas.application.factories.tarea_factory import TareaFactory

tarea = TareaFactory.crear_tarea(
    "Ir a dormir", "Eacostarme y descansar", "pendiente", "urgente")
print(tarea.mostrar_info())
