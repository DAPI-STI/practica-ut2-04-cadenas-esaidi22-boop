"""
Ejercicio 3: leer un nombre y mostrarlo en mayúsculas y cuántas letras tiene.

La función devolverá una tupla:
(nombre_en_mayusculas, numero_de_letras_sin_espacios)
"""


def name_upper_and_length(name: str) -> tuple[str, int]:
    nombre_mayus = name.upper()
    letras_sin_espacios = len(name.replace(" ", ""))
    return nombre_mayus, letras_sin_espacios
