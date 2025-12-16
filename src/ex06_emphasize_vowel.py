"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.

La función debe:
- Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.
- Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.
- Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(phrase: str, vowel: str) -> str:
    if len(vowel) != 1 or vowel.lower() not in "aeiou":
        raise ValueError("La vocal debe ser un solo carácter y una vocal válida (a, e, i, o, u)")
    
    vowel_lower = vowel.lower()
    result = ""
    for ch in phrase:
        if ch.lower() == vowel_lower:
            result += ch.upper()
        else:
            result += ch
    return result

# Frase y vocal a enfatizar
frase = "bachir come patatas"
vocal = "a"

resultado = emphasize_vowel(frase, vocal)
print("Frase original:", frase)
print("Vocal a enfatizar:", vocal)
print("Frase con vocal enfatizada:", resultado)

