"""
Escribir un programa, llamado rot13.py que reciba un archivo de texto de origen
y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea
cifrada en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada
carácter comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para
obtener un nuevo carácter.
"""

try:
    archivo = open('fundacion.txt')
    archivoEncrypted = open('encrypted_fundación.txt', 'w')
    linea = archivo.readline()

    while linea:
        desencrypted = []

        for letra in linea:
            if 'a' <= letra <= 'z':
                desencrypted.append(chr((ord(letra) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= letra <= 'Z':
                desencrypted.append(chr((ord(letra) - ord('A') + 13) % 26 + ord('A')))
            else:
                desencrypted.append(letra)

        archivoEncrypted.write("".join(desencrypted))
        linea = archivo.readline()

    archivo.close()
    archivoEncrypted.close()
except FileNotFoundError:
    print('[!] Error en el proceso')