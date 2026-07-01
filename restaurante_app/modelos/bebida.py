from modelos.producto import Producto

# HERENCIA: Bebida hereda de Producto
class Bebida(Producto):
    """Clase hija que representa una bebida de la carta."""

    def __init__(self, nombre: str, precio_inicial: float, disponible: bool, volumen_ml: int):
        # Uso de super() para reutilizar el constructor de la clase padre
        super().__init__(nombre, precio_inicial, disponible)
        self.volumen_ml: int = volumen_ml

    # SOBRESCRITURA DE MÉTODO (Polimorfismo)
    def mostrar_informacion(self) -> str:
        info_padre = super().mostrar_informacion()
        return f"[Bebida] {info_padre} | Tamaño: {self.volumen_ml} ml"