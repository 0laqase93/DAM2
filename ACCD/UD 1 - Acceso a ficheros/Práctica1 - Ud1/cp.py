"""
Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo
a otro, de modo que quede exactamente igual.
"""

try:
    archive = open("fundacion.txt")
    archiveCopy = open("fundacionCopy.txt", "w")

    archiveCopy.write(archive.read())
    archive.close()
    archiveCopy.close()

    print("[+] Archivo copiado con éxito")
except ValueError:
    print("[!] Fallo en la operación de copiado")