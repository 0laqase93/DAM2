"""
Definir una lista con un conjunto de nombres, imprimir la cantidad que comienzan con la letra
a. También se puede hacer elegir al usuario la letra a buscar. (Un poco más emocionante)
"""

nombres = ["Ana", "Luis", "Carlos", "María", "Jorge", "Lucía", "Pedro", "Elena", "Raúl", "Sofía"]

letter = input("[+] Ingrese la letra por que quiere buscar: ").upper()

print("[+] Los nombres que empiezan con esa letra son: ")
for nombre in nombres:
    if nombre[0] == letter:
        print(f"-> {nombre}")
