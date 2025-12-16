"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:
- Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".
- Devuelve (dia, mes, año) como enteros.
- Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    parts = date_str.strip().split("/")
    
    if len(parts) != 3:
        raise ValueError("Formato de fecha incorrecto. Debe ser dd/mm/aaaa")
    
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError:
        raise ValueError("Día, mes y año deben ser números enteros")
    
    if not (1 <= day <= 31):
        raise ValueError("Día fuera de rango (1-31)")
    if not (1 <= month <= 12):
        raise ValueError("Mes fuera de rango (1-12)")
    
    return day, month, year


fechas = ["09/12/2025", "9/1/2025"]

for f in fechas:
    d, m, a = parse_date(f)
    print(f"Fecha: {f} -> Día: {d}, Mes: {m}, Año: {a}")
