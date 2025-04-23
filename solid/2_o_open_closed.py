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
# • Refactoriza para que el sistema esté abierto a nuevos tipos de notificación sin
# modificar NotificationService.
