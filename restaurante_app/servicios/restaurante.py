from modelos.producto import Producto

class Restaurante:
    """Clase de servicio encargada de administrar y listar los productos."""

    def __init__(self, nombre_sucursal: str):
        self.nombre_sucursal: str = nombre_sucursal
        # Lista compuesta para almacenar cualquier objeto derivado de Producto
        self.catalogo_productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        """Añade un producto al catálogo."""
        self.catalogo_productos.append(producto)

    def mostrar_menu_completo(self) -> None:
        """POLIMORFISMO: Recorre la lista llamando al mismo método, pero actúa diferente."""
        print(f"\n================ MENÚ DIGITAL: {self.nombre_sucursal.upper()} ================")
        if not self.catalogo_productos:
            print("El catálogo está vacío actualmente.")
            return

        for producto in self.catalogo_productos:
            # Aquí se demuestra el polimorfismo: Python decide en tiempo de ejecución
            # si llama a mostrar_informacion() de Platillo o de Bebida.
            print(producto.mostrar_informacion())
        print("===================================================================\n")