"""
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva
las palabras que tengan más de n caracteres.
"""

list = ["uno", "dos", "tres", "cuatro", "cinco"]

def filtrar_palabras(list, num):
    aux = []
    for i in list:
        if len(i) > num:
            aux.append(i)
    return aux

print(filtrar_palabras(list, 4))