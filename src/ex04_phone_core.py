"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str:
    s = s.strip()
    partes = s.split("-")
    if len(partes) != 3:
        raise ValueError
    if not partes[0].startswith("+"):
        raise ValueError
    if not partes[1].isdigit():
        raise ValueError
    return partes[1]

print("EX04:")
telefono = "+34-913724710-56"
print("Número central:", phone_core(telefono))
print("-" * 40)
