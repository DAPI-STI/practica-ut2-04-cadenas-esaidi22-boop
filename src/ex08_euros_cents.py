"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:
- Recibe una cadena como "123.45" o "123,45".
- Devuelve una tupla (euros, centimos) como enteros.
- Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    s = price_str.strip().replace(",", ".")
    parts = s.split(".")
    
    # Validación
    if len(parts) != 2 or len(parts[1]) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        raise ValueError("El precio debe tener exactamente dos decimales y ser numérico")
    
    euros = int(parts[0])
    cents = int(parts[1])
    return euros, cents


result = euros_cents("300,10")
print("Euros:", result[0])
print("Céntimos:", result[1])







