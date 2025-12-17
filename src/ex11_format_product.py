"""
Ejercicio 11: formatear información de un producto (nombre, precio, unidades).

La función:
- Recibe nombre (str), precio (float) y unidades (int).
- Devuelve una cadena formateada con:
  nombre
  precio unitario con 6 dígitos enteros y 2 decimales
  unidades con 3 dígitos (relleno con ceros)
  coste total (precio * unidades) con 8 enteros y 2 decimales
"""
def format_product(name: str, price: float, units: int) -> str:
    """
    Formatea un producto con:
    - precio unitario: 6 enteros + 2 decimales
    - unidades: 3 dígitos con ceros
    - coste total: 8 enteros + 2 decimales
    """
    total = price * units
    return (
        f"Nombre: {name}\n"
        f"Precio unitario: {price:09.2f} €\n"
        f"Unidades: {units:03d}\n"
        f"Coste total: {total:011.2f} €"
    )