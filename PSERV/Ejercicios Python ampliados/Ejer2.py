"""
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.
"""

list = ["uno", "dos", "tres", "cuatro", "cinco"]

def mas_larga(list):
    return max(list, key=len)

print(mas_larga(list))