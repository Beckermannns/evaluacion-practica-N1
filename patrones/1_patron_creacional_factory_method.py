# Descripción:
# Necesitas crear distintos tipos de tareas: TareaNormal, TareaUrgente,
# TareaProgramada. Actualmente todo se instancia con new.
# Tarea:
# • Crea una jerarquía de clases Tarea con subclases específicas.
# • Implementa un Factory Method para encapsular la lógica de creación.
# Patrón Estructural – Decorator
# Descripción:
# Quieres agregar características adicionales a las tareas (por ejemplo: "Con archivo adjunto",
# "Marcada como importante") sin modificar la clase original Tarea.
# Tarea:
# • Usa el patrón Decorator para extender funcionalidades.
# • Permite combinar múltiples decoradores (por ejemplo: TareaUrgente + Adjuntos).
