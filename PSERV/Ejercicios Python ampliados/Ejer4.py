"""
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que
evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def filtrar_palabras(text):
    return sum(1 for t in text if t.isupper())

text = input("[+] Introduzca una cadena: ")

print(filtrar_palabras(text))