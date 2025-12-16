"""
Ejercicio 3: leer un nombre y mostrarlo en mayúsculas y cuántas letras tiene.

La función devolverá una tupla:
(nombre_en_mayusculas, numero_de_letras_sin_espacios)
"""


def name_upper_and_length(name: str) -> tuple[str, int]:
    return name.upper(), len(name.replace(" ", ""))
nombre = input("BACHIR SAIDIB: ")
nombre_mayus, numero_letras = name_upper_and_length(nombre)
print(nombre_mayus)
print(numero_letras)






   