# 3. LSP – Sustitución de Liskov
# Código base:
# public class Bird {
#   public void fly() {
#          System.out.println("Flying");
#   }
# }
# public class Penguin extends Bird {
#   @Override
#   public void fly() {
#       throw new UnsupportedOperationException("Penguins can't fly");
#   }
# }

# Tarea:
# • Detecta la violación a LSP.
# • Refactoriza para que se respete el principio.
