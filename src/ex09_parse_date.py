"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
 parts = date_str.split("/")
    if len(parts) != 3:
        raise ValueError("Formato de fecha incorrecto. Debe ser dd/mm/aaaa")
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError: