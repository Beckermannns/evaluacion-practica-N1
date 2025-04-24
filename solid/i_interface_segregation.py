# 4. ISP – Segregación de Interfaces
# Código base:
# public interface Animal {
#   void walk();
#   void fly();
#   void swim();
# }
# public class Dog implements Animal {
#   public void walk() {
#       System.out.println("Dog walking");
#   }
#   public void fly() {
#       throw new UnsupportedOperationException("Dogs can't fly");
#   }
#   public void swim() {
#       System.out.println("Dog swimming");
#   }
# }

# Tarea:
# • Identifica los métodos innecesarios en ciertas clases.
# • Divide la interfaz en múltiples interfaces específicas por comportamiento
# (Walkable, Swimmable, Flyable).
# • Refactoriza Dog para implementar solo lo que realmente necesita.


######################### DESARROLLO #########################
# En primer lugar, identifiqué que la interfaz Animal tiene métodos innecesarios para ciertas clases.
# Para este caso creo que lo mejor es dividirla en otras interfaces mas específicas por comportamiento.
# Luego cada clase implementa solo lo que realmente necesita, en este caso la clase Dog solo implementa la interfaz Caminar y Nadar.

# Código refactorizado:

from abc import ABC, abstractmethod


class Animal(ABC):  # Clase base para los animales
    @abstractmethod
    def hacer_sonido(self):
        pass    # Método abstracto


class Nadar(ABC):  # Interfaz para nadar
    @abstractmethod
    def nadar(self):
        pass


class Volar(ABC):  # Interfaz para volar
    @abstractmethod
    def volar(self):
        pass


class Caminar(ABC):  # Interfaz para caminar
    @abstractmethod
    def caminar(self):
        pass


class Pato(Animal, Volar, Nadar):  # Ejemplo de pato que implementa las interfaces Volar y Nadar
    def __init__(self, nombre):
        self.nombre = nombre

    def volar(self):
        print("El pato está volando.")

    def nadar(self):
        print("El pato está nadando.")

# Finalmente la clase Perro implementa la interfaz Nadar, ya que no vuela.
# Esto permite que la clase Perro no tenga que implementar el método volar() y,
# por lo tanto, no violamos el principio de sustitución de Liskov y de paso el principio de segregación de interfaces.


class Perro(Animal, Nadar, Caminar):
    def __init__(self, nombre):
        self.nombre = nombre

    def nadar(self):
        print("El perro está nadando.")

    def hacer_sonido(self):
        print("El perro hace guau.")

    def caminar(self):
        print("El perro está caminando.")
