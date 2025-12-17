"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.

La función debe:

Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.

Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.

Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(phrase: str, vowel: str) -> str:
    """
    Convierte a mayúscula todas las apariciones de vowel en la frase.
    Sugerencia:
    - Comprueba que vowel es un solo carácter y está en "aeiou" (en minúscula).
    - Recorre la frase carácter a carácter y construye una nueva cadena.
    """
  def emphasize_vowel(phrase: str, vowel: str) -> str:
    if len(vowel) != 1:
        raise ValueError("La vocal debe ser un solo carácter")

    v = vowel.lower()
    if v not in "aeiou":
        raise ValueError("La letra introducida no es una vocal")

    resultado = []
    for char in phrase:
        if char.lower() == v:
            resultado.append(char.upper())
        else:
            resultado.append(char)

    return "".join(resultado)

