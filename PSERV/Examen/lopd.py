import sys
from colorama import init, Fore
init()

n = 5
try:
    if 2 <= len(sys.argv) <= 3:
        if len(sys.argv) == 3:
            if int(sys.argv[1]) >= 0:
                if int(sys.argv[1]) >= 9:
                    n = 9
                else:
                    n = int(sys.argv[1])

        encriptado = []
        archivo = open(sys.argv[len(sys.argv) - 1], 'r')
        archivoEncriptado = open(f'{sys.argv[len(sys.argv) - 1]}_lopd', 'w')
        linea = archivo.readline()

        while linea:
            partes = linea.split()
            partes[0] = "*" * n + partes[0][n::]
            encriptado.append(partes[0] + " " + partes[1])
            for i in range(2, len(partes)):
                partes[i] = partes[i][0:2] + (len(partes[i]) - 2) * "*"
                encriptado.append(" " + partes[i])

            encriptado.append("\n")
            linea = archivo.readline()

        archivoEncriptado.write("".join(encriptado))
        archivo.close()
        archivoEncriptado.close()
        print(f"{Fore.GREEN}[+]{Fore.RESET} Archivo encriptado creado con éxito.")
    else:
        print(f"{Fore.RED}[!]{Fore.RESET} Se debe ejecutar con el siguiente formato: lopd [n] fichero")
except FileNotFoundError:
    print(f"{Fore.RED}[!]{Fore.RESET} Error en el proceso")