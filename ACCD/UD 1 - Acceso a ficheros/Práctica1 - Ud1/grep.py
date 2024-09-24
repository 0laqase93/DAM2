"""
Escribir un programa, llamado grep.py que reciba una expresión y un archivo e
imprima las líneas del archivo que contienen la expresión recibida.
"""

try:
    nombreArchivo = input('[+] Inserte el archivo: ')
    archivo = open(nombreArchivo)
    expr = input('[+] Inserte la expresión que desea buscar: ').lower()
    linea  = archivo.readline().lower()
    while linea:
        if expr in linea:
            linea = linea.replace(expr, '\033[1m' + '\033[32m' + expr + '\033[0m')
            print(linea, end="")
        linea = archivo.readline().lower()

except FileNotFoundError:
    print("[!] Error en el proceso")