"""
Ejercicio 10: leer una lista de productos separados por comas y mostrar cada uno en una línea.
La función:
Recibe una cadena tipo "pan, leche, huevos".
Devuelve una lista con ["pan", "leche", "huevos"], sin espacios sobrantes.
"""
def split_products(csv_line: str) -> list[str]:
    """
    Recibe una cadena de productos separados por comas y devuelve
    una lista con cada producto sin espacios sobrantes.
    """
    return [item.strip() for item in csv_line.split(",")]
