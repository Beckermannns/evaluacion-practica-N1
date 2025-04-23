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
