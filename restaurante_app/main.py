import sys
import os

# Solución definitiva para rutas en PyCharm/Consola:
# Asegura que el directorio raíz 'restaurante_app' esté en el camino de búsqueda de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicios.restaurante import Restaurante
from modelos.platillo import Platillo
from modelos.bebida import Bebida

def iniciar_programa():
    # Instanciamos el servicio
    mi_restaurante = Restaurante("Gourmet Express")

    # Crear dos objetos de tipo Platillo
    platillo_uno = Platillo("Hamburguesa Artesanal", 9.99, True, 650)
    platillo_dos = Platillo("Ensalada César con Pollo", 7.50, True, 350)

    # Crear dos objetos de tipo Bebida
    bebida_uno = Bebida("Limonada Imperial", 2.50, True, 500)
    bebida_dos = Bebida("Té Frío de Durazno", 2.00, False, 400)

    # Agregar los objetos al servicio principal
    mi_restaurante.agregar_producto(platillo_uno)
    mi_restaurante.agregar_producto(platillo_dos)
    mi_restaurante.agregar_producto(bebida_uno)
    mi_restaurante.agregar_producto(bebida_dos)

    # Mostrar la información en consola aplicando Polimorfismo
    mi_restaurante.mostrar_menu_completo()

    # Demostración opcional del Setter y las Validaciones (Encapsulación)
    print("--> Intentando cambiar el precio a un valor negativo...")
    platillo_uno.cambiar_precio(-5.00) # Debería lanzar error por consola sin alterar el original

    print("\n--> Modificando un precio con éxito:")
    bebida_uno.cambiar_precio(3.00) # Cambio válido
    mi_restaurante.mostrar_menu_completo()

if __name__ == "__main__":
    iniciar_programa()