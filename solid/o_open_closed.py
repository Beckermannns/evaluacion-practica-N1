# 2. OCP – Abierto/Cerrado
# Código base:
# public class NotificationService {
#   public void send(String type, String message) {
#       if (type.equals("EMAIL")) {
#           System.out.println("Sending EMAIL: " + message);
#       } else if (type.equals("SMS")) {
#           System.out.println("Sending SMS: " + message);
#       }
#   }
# }

# Tarea:
# • Refactoriza para que el sistema esté abierto a nuevos tipos de notificación sin modificar NotificationService.

######################### DESARROLLO #########################

# Clase base para el servicio de notificación, esta es la plantilla que usare para los servicios de notificación
# que se implementarán posteriormente. Utiliza el módulo abc para definir métodos abstractos.
# Esto deja la funcionalidad abierta a la extensión, ya que se pueden agregar nuevos tipos de notificaciones sin modificar la clase base.
# Pero cerrada a la modificación, ya que no se puede cambiar la lógica de envío de notificaciones en la clase base.

# Código refactorizado:
from abc import ABC, abstractmethod


class ServicioNotificacion(ABC):
    @abstractmethod
    def enviar(self, message):    # Método abstracto para enviar notificaciones
        pass

# Un ejemplo del uso de la clase ServicioNotificacion para crear una clase EmailNotificationService que hereda de ServicioNotificacion.
# Esta clase implementa el método enviar para enviar notificaciones por correo electrónico.


class ServicioNotificacionEmail(ServicioNotificacion):
    # Implementación del método send para enviar notificaciones por correo electrónico
    def enviar(self, message):
        return f"Enviando EMAIL: {message}"

# Otro ejemplo del uso de la clase ServicioNotificacion puede ser el de enviar mensajes de texto,
# para eso creo una clase SMSNotificationService que hereda de ServicioNotificacion.
# Esta clase implementa el método send para enviar notificaciones por SMS.


class NotificacionServicioSMS(ServicioNotificacion):
    def enviar(self, message):    # Implementación del método enviar para enviar notificaciones por SMS
        return f"Enviando SMS: {message}"
