# main.py

from patrones.tareas.application.factories.tarea_factory import TareaFactory
from patrones.tareas.domain.decorators import TareaConAdjunto, TareaImportante, TareaResponsable
from patrones.tareas.domain.strategy.context.sorter import Sorter
from patrones.tareas.domain.strategy.strategy.state_sort import StateSortStrategy
from patrones.tareas.domain.strategy.strategy.title_sort import TitleSortStrategy
from patrones.tareas.domain.strategy.strategy.type_sort import TypeSortStrategy

if __name__ == "__main__":
    ######################### Crear tareas usando Factory Method #########################
    tarea1 = TareaFactory.crear_tarea(
        "Hacer informe", "Detalles del informe...", "Pendiente", "normal")
    tarea2 = TareaFactory.crear_tarea(
        "Reunión urgente", "Discusión crítica...", "En progreso", "urgente")
    tarea3 = TareaFactory.crear_tarea(
        "Planificar sprint", "Definir objetivos...", "Pendiente", "programada")
    tarea4 = TareaFactory.crear_tarea(
        "Revisar código", "Buscar errores...", "Completada", "normal")

    tareas = [tarea1, tarea2, tarea3, tarea4]

    print("Tareas creadas con Factory Method:")
    for tarea in tareas:
        print(tarea.mostrar_info(
        ) + f" - Estado: {tarea.estado}, Título: {tarea.titulo}, Tipo: {tarea.tipo}")
    print("-" * 20)

    ######################### Decorar tareas #########################
    tarea1_con_adjunto = TareaConAdjunto(tarea1, "informe_final.docx")
    tarea2_importante = TareaImportante(tarea2)
    tarea3_responsable = TareaResponsable(tarea3, "Ana Pérez")
    tarea4_importante_con_adjunto_responsable = TareaResponsable(
        TareaConAdjunto(TareaImportante(tarea4), "revision.txt"), "Carlos López")

    print("Tareas decoradas:")
    print(tarea1_con_adjunto.mostrar_info())
    print(tarea2_importante.mostrar_info())
    print(tarea3_responsable.mostrar_info())
    print(tarea4_importante_con_adjunto_responsable.mostrar_info())
    print("-" * 20)

    ######################### Crear las estrategias de ordenamiento #########################
    orden_por_estado = StateSortStrategy()
    orden_por_titulo = TitleSortStrategy()
    orden_por_tipo = TypeSortStrategy()

    ######################### Crear el contexto (Sorter) y establecer la estrategia inicial (por estado) #########################
    sorter = Sorter(orden_por_estado)

    print("Tareas ordenadas por estado:")
    tareas_ordenadas_estado = sorter.sort(list(tareas))
    for tarea in tareas_ordenadas_estado:
        print(tarea.mostrar_info(
        ) + f" - Estado: {tarea.estado}, Título: {tarea.titulo}, Tipo: {tarea.tipo}")
    print("-" * 20)

    ######################### Cambiar la estrategia y ordenar por título #########################
    sorter.set_strategy(orden_por_titulo)
    print("Tareas ordenadas por título:")
    tareas_ordenadas_titulo = sorter.sort(list(tareas))
    for tarea in tareas_ordenadas_titulo:
        print(tarea.mostrar_info(
        ) + f" - Estado: {tarea.estado}, Título: {tarea.titulo}, Tipo: {tarea.tipo}")
    print("-" * 20)

    ######################### Cambiar la estrategia y ordenar por tipo #########################
    sorter.set_strategy(orden_por_tipo)
    print("Tareas ordenadas por tipo:")
    tareas_ordenadas_tipo = sorter.sort(list(tareas))
    for tarea in tareas_ordenadas_tipo:
        print(tarea.mostrar_info(
        ) + f" - Estado: {tarea.estado}, Título: {tarea.titulo}, Tipo: {tarea.tipo}")
    print("-" * 20)
