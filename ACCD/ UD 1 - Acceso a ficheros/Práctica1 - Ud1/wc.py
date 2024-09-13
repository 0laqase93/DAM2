"""
Escribir un programa, llamado wc.py que reciba un archivo, lo procese e
imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el
archivo.
"""

try:
    archivo = open('fundacion.txt')
    linea = archivo.readline()
    lineas = 0
    palabras = 0
    caracteres = 0

    while linea:
        linea = archivo.readline()
        lineas += 1
        palabras += len(linea.split(" "))
        caracteres += len(linea)

    print(f"[+] El archivo tiene {lineas} lineas, {palabras} palabras y {caracteres} caracteres")

    archivo.close()
except FileNotFoundError:
    print("[!] Error en el proceso")