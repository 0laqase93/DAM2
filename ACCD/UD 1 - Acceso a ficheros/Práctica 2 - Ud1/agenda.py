import csv
from colorama import init, Fore
import os

init()

ARCHIVO = 'agenda.csv'

def readcsv():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, 'r', newline='', encoding='utf-8') as csvfile:
        contenido = csv.reader(csvfile, delimiter=';')
        datos = list(contenido)
        return datos

def writecsv(datos):
    with open(ARCHIVO, 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile, delimiter=';')
        escritor.writerows(datos)

def createMenu(title, options):
    large = len(title) + 7
    for i in options:
        if large < len(i) + 7:
            large = len(i) + 7

    menu = "┌" + "─" * (large + 1) + "┐\n"
    centre = (large - len(title)) / 2
    menu += "│" + " " + Fore.YELLOW + title + Fore.RESET + " " * (large - len(title)) + "│\n"
    menu += "├" + "─" * (large + 1) + "┤\n"

    cont = 1
    large += 1
    for i in options:
        menu += f"│ {Fore.GREEN}{cont}{Fore.RESET} -> {i} {" " * (large - len(i) - 8)} │\n"
        cont += 1

    menu += "└" + "─" * large + "┘"

    return menu


def showMenu(menu, options):
    print(menu)

    option = -1
    while option <= 0 or option > len(options):
        try:
            option = int(input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte una opción: "))
        except ValueError:
            print("[!] Opción no válida.")
    return option


def guardarDatos():
    nombre = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el nombre del usuario: ")
    apellido = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el apellido del usuario: ")
    email = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el email del usuario: ")
    tel1 = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el primer teléfono del usuario: ")
    tel2 = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el segundo teléfono del usuario (opcional): ")
    direccion = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte la dirección del usuario: ")

    with open(ARCHIVO, 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo, delimiter=';')
        writer.writerow([nombre, apellido, email, tel1, tel2, direccion])
        print("Contacto guardado con éxito.")


def modificarDatos():
    datos = readcsv()
    nombre = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el nombre o apellido del contacto a modificar: ")

    for index, fila in enumerate(datos):
        if nombre in fila:
            print(f"{Fore.YELLOW}[+]{Fore.RESET} Contacto encontrado: {fila}")
            datos[index][0] = input(f"Nuevo nombre [{fila[0]}]: ") or fila[0]
            datos[index][1] = input(f"Nuevo apellido [{fila[1]}]: ") or fila[1]
            datos[index][2] = input(f"Nuevo email [{fila[2]}]: ") or fila[2]
            datos[index][3] = input(f"Nuevo teléfono 1 [{fila[3]}]: ") or fila[3]
            datos[index][4] = input(f"Nuevo teléfono 2 [{fila[4]}]: ") or fila[4]
            datos[index][5] = input(f"Nuevo dirección [{fila[5]}]: ") or fila[5]
            writecsv(datos)
            print(f"{Fore.GREEN}[+]{Fore.RESET} Contacto modificado con éxito.")
            return
    print(f"{Fore.RED}[-]{Fore.RESET} Contacto no encontrado.")


def darBaja():
    datos = readcsv()
    nombre = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el nombre o apellido del contacto a eliminar: ")

    for index, fila in enumerate(datos):
        if nombre in fila:
            print(f"{Fore.YELLOW}[+]{Fore.RESET} Eliminando contacto: {fila}")
            datos.pop(index)
            writecsv(datos)
            print(f"{Fore.GREEN}[+]{Fore.RESET} Contacto eliminado con éxito.")
            return
    print(f"{Fore.RED}[-]{Fore.RESET} Contacto no encontrado.")


def buscarDato():
    datos = readcsv()

    if not datos:
        print(f"{Fore.RED}[-]{Fore.RESET} No hay contactos para buscar.")
        return

    nombre = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el nombre o apellido del contacto a buscar: ")

    for fila in datos[1:]:
        if nombre in fila:
            print(f"{Fore.GREEN}[+]{Fore.RESET} Contacto encontrado.")

            anchos = [max(len(str(item)) for item in columna) + 2 for columna in zip(datos[0], fila)]

            def crear_fila(valores, es_titulo=False):
                fila = "║"
                for i, valor in enumerate(valores):
                    fila += f" {valor.ljust(anchos[i])} ║" if es_titulo else f" {valor.ljust(anchos[i])} ║"
                return fila

            def crear_separador(tipo="medio"):
                separador = "╠" if tipo == "medio" else "╔"
                for ancho in anchos:
                    separador += "═" * (ancho + 2)
                    separador += "╬" if tipo == "medio" else "╦"
                separador = separador[:-1] + ("╣" if tipo == "medio" else "╗")
                return separador

            def crear_final():
                final = "╚"
                for ancho in anchos:
                    final += "═" * (ancho + 2)
                    final += "╩"
                return final[:-1] + "╝"

            # Mostrar el encabezado
            print(crear_separador("inicio"))
            print(crear_fila(datos[0], es_titulo=True))
            print(crear_separador("medio"))
            print(crear_fila(fila))
            print(crear_final())
            return

    print(f"{Fore.RED}[-]{Fore.RESET} Contacto no encontrado.")

def mostrarDato():
    datos = readcsv()

    if not datos:
        print(f"{Fore.RED}[-]{Fore.RESET} No hay contactos para mostrar.")
        return

    columnas = list(zip(*datos))
    anchos = [max(len(str(item)) for item in columna) + 2 for columna in columnas]

    def crear_fila(valores, es_titulo=False):
        fila = "║"
        for i, valor in enumerate(valores):
            fila += f" {valor.ljust(anchos[i])} ║" if es_titulo else f" {valor.ljust(anchos[i])} ║"
        return fila

    def crear_separador(tipo="medio"):
        separador = "╠" if tipo == "medio" else "╔"
        for ancho in anchos:
            separador += "═" * (ancho + 2)
            separador += "╬" if tipo == "medio" else "╦"
        separador = separador[:-1] + ("╣" if tipo == "medio" else "╗")
        return separador

    def crear_final():
        final = "╚"
        for ancho in anchos:
            final += "═" * (ancho + 2)
            final += "╩"
        return final[:-1] + "╝"

    print(crear_separador("inicio"))
    print(crear_fila(datos[0], es_titulo=True))
    print(crear_separador("medio"))

    for fila in datos[1:]:
        print(crear_fila(fila))
    print(crear_final())


titleMenu = "MENÚ AGENDA"
optionsMenu = [
    "Guardar datos",
    "Modificar datos",
    "Dar de baja",
    "Buscar",
    "Mostrar",
    "Salir"
]
menu = createMenu(titleMenu, optionsMenu)

while True:
    option = showMenu(menu, optionsMenu)

    match option:
        case 1:
            guardarDatos()
        case 2:
            modificarDatos()
        case 3:
            darBaja()
        case 4:
            buscarDato()
        case 5:
            mostrarDato()
        case 6:
            print(f"{Fore.RED}[+] Saliendo del programa...{Fore.RESET}")
            exit()