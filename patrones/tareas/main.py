from patrones.tareas.application.factories.tarea_factory import TareaFactory
from patrones.tareas.domain.decorators import TareaConAdjunto, TareaImportante, TareaResponsable

if __name__ == "__main__":
    # Crear tareas usando Factory Method
    tarea1 = TareaFactory.crear_tarea(
        "Hacer informe", "Detalles del informe...", "Pendiente", "normal")
    tarea2 = TareaFactory.crear_tarea(
        "Reunión urgente", "Discusión crítica...", "En progreso", "urgente")
    tarea3 = TareaFactory.crear_tarea(
        "Planificar sprint", "Definir objetivos...", "Pendiente", "programada")

    print("Tareas sin decorar:")
    print(tarea1.mostrar_info())
    print(tarea2.mostrar_info())
    print(tarea3.mostrar_info())
    print("-" * 20)

    # Decorar tareas con los decoradroes generados
    tarea1_con_adjunto = TareaConAdjunto(tarea1, "informe_final.docx")
    tarea2_importante = TareaImportante(tarea2)
    tarea3_importante_con_adjunto = TareaConAdjunto(TareaImportante(
        tarea3), "plan_detallado.pdf")  # Combinación de dos decoradores
    # Decorador para asignar un responsable
    tarea4_responsable = TareaResponsable(tarea1, "Brian Fuentes")
    # Decorador para asignar un responsable a una tarea importante
    tarea5_responsable_importante = TareaResponsable(
        tarea2_importante, "Esteban Ramirez")

    print("Tareas decoradas:")
    print(tarea1_con_adjunto.mostrar_info())
    print(tarea2_importante.mostrar_info())
    print(tarea3_importante_con_adjunto.mostrar_info())
    print(tarea4_responsable.mostrar_info())
    print(tarea5_responsable_importante.mostrar_info())
