class Producto:

    def __init__(self, nombre: str, precio_inicial: float, disponible: bool):
        self.nombre: str = nombre
        # ENCAPSULACIÓN
        self.__precio: float = 0.0
        self.disponible: bool = disponible

        # Asignamos el precio usando el validador
        self.cambiar_precio(precio_inicial)

    # MÉTODOS DE ACCESO
    def obtener_precio(self) -> float:
        """Devuelve el precio protegido del producto."""
        return self.__precio

    # MÉTODOS DE MODIFICACIÓN
    def cambiar_precio(self, nuevo_precio: float) -> None:
        """Valida que el precio no sea negativo ni cero antes de asignarlo."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"[Error]: El precio para '{self.nombre}' debe ser mayor a cero. No se aplicó el cambio.")

    def mostrar_informacion(self) -> str:
        """Método base que será sobrescrito por las clases hijas."""
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Nombre: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"