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

######################### DESARROLLO #########################
# Lo primero es identificar la violación a LSP, que es el hecho de que la clase Penguin hereda de Bird y no puede volar.
# Para solucionar esto, separamos la funcionalidad de volar en una interfaz y creamos una clase base para los pájaros que no vuelan.
# De esta manera, la clase Penguin no hereda de FlyingBird, sino de una clase base que representa a los pájaros que no vuelan NonFlyingBird.
# Esto permite que la clase Penguin no tenga que implementar el método fly() y, por lo tanto, no violamos el principio de sustitución de Liskov.


# Código refactorizado:
class AveVoladora:
    def volar(self):  # Método para volar
        return "Volando"


class AveNoVoladora:
    def caminar(self):  # Método para caminar
        return "Caminando"


class Paloma(AveVoladora):  # Clase para los pájaros que vuelan
    def volar(self):
        return "Volando"


class Gallina(AveNoVoladora):  # Clase para los pájaros que no vuelan
    def caminar(self):  # Método para caminar
        return "Caminando"
