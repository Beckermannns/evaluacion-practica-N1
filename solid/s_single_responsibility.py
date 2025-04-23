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

# Código refactorizado:

class ReportGenerator:
    def generate(self, data):
        return f"Generando reporte con: {data}"


class FileSaver:
    def save(self, content):
        return f"Guardando reporte en archivo: {content}"


class EmailSender:
    def send(self, email, content):
        return f"Enviando {content} a email: {email}"
