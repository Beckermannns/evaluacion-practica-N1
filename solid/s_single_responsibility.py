# 1. SRP – Responsabilidad Única
# Código base:
# public class ReportManager {
#   public void generateReport(String data) {
#       System.out.println("Generating report with: " + data);
#   }
#   public void saveToFile(String content) {
#       System.out.println("Saving report to file: " + content);
#   }
#   public void sendEmail(String email, String content) {
#       System.out.println("Sending report to email: " + email);
#   }
# }

# Tarea:
# • Identifica las responsabilidades múltiples.
# • Refactoriza el código aplicando SRP.

######################### DESARROLLO #########################
# Primero identifique 3 funciones para la misma clase, que son generar un reporte, guardar el reporte y enviar el reporte por email.
# Luego cree 3 clases diferentes para cada una de las funciones, y cada clase tiene su propia función. De esta menera cada clase tiene una sola responsabilidad.

# Código refactorizado:

class GeneradorReporte:  # Clase para generar reportes
    def generar(self, data):   # Su respectiva función para generar un reporte
        return f"Generando reporte con: {data}"


class GuardarArchivo:    # Clase para guardar reportes
    def guardar(self, content):    # Su respectiva función para guardar un reporte
        return f"Guardando reporte en archivo: {content}"


class EnviarEmail:  # Clase para enviar reportes por email
    def enviar(self, email, content):  # Su respectiva función para enviar un reporte por email
        return f"Enviando {content} a email: {email}"
