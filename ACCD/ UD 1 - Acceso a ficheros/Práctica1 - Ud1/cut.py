"""
Escribir un programa, llamado cut.py, que dado un archivo de texto, un
delimitador, y una lista de campos, imprima solamente esos campos, separados por ese
delimitador.
"""

try:
    archivo = open("listado-codigos-postales.csv")
    delimi = input("[+] Inserte el delimitador que separa los campos: ")
    campos = archivo.readline()[:-1].split(delimi)
    print("[+] MENÚ [+]")
    cont = 1

    for campo in campos:
        print(f"{cont} - {campo}")
        cont += 1

    camposEscogidos = input("[+] Inserte el número del campo separado por un espacio: ").split(" ")
    linea = archivo.readline()

    delimi2 = " " + input("[+] Inserte el delimitador: ") + " "

    while linea != "":
        imprimir = ""

        for campoEscogido in camposEscogidos:
            if 0 < int(campoEscogido) < cont:
                imprimir += linea.split(delimi)[int(campoEscogido) - 1] + delimi2
            else:
                camposEscogidos.remove(campoEscogido)

        print(imprimir[:-2])
        linea = archivo.readline()

    archivo.close()
except FileNotFoundError:
    print("[!] Error en el proceso")