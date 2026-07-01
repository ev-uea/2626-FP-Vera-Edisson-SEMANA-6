from modelos.producto import Producto

# HERENCIA: Platillo hereda de Producto
class Platillo(Producto):
    """Clase hija que representa una comida o plato específico."""

    def __init__(self, nombre: str, precio_inicial: float, disponible: bool, calorias: int):
        # Uso de super() para reutilizar el constructor de la clase padre
        super().__init__(nombre, precio_inicial, disponible)
        self.calorias: int = calorias

    # SOBRESCRITURA DE MÉTODO (Polimorfismo)
    def mostrar_informacion(self) -> str:
        # Obtenemos la información base y le concatenamos el atributo específico
        info_padre = super().mostrar_informacion()
        return f"[Platillo] {info_padre} | Calorías: {self.calorias} kcal"