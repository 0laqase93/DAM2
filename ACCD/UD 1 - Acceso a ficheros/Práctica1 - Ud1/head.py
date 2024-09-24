"""
Escribir un programa, llamado head que reciba un archivo y un número N e
imprima las primeras N líneas del archivo.
"""

try:
    archive = open("fundacion.txt")
    n = int(input("[+] Inserte el número de líneas que quiere leer: "))

    for i in range(n):
        print(archive.readline(), end="")

    archive.close()
except ValueError:
    print("[!] No has insertado un número")