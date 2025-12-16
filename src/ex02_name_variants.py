"""
Ejercicio 2: leer un nombre completo (nombre + apellidos) y mostrar:

Todo en minúsculas.

Todo en mayúsculas.

Capitalizado (primera letra de cada palabra en mayúscula).

La función devolverá una tupla: (minusculas, mayusculas, capitalizado).
"""
def name_variants(full_name: str) -> tuple[str, str, str]:
    return full_name.lower(), full_name.upper(), full_name.title()
nombre = input("BACHIR SAIDI: ")
minusculas, mayusculas, capitalizado = name_variants(nombre)
print(minusculas)
print(mayusculas)
print(capitalizado)



  
   
 