# Importar librerías
import csv
from colorama import init, Fore

init()

# Variables
contenido = ''

def readcsv():
    with open('agenda.csv', 'r', newline='') as csvfile:
        contenido = csv.reader(csvfile, delimiter=';')
        datos = list(contenido)
        return datos

# Escribir archivo CSV
def writecsv(datos):
    with open('agenda.csv', 'w', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter=';')
        escritor.writerows(datos)

# Crear menú de forma dinámica
def createMenu(title, options):
    large = len(title) + 7
    for i in options:
        if large < len(i) + 7:
            large = len(i) + 7

    # Generar título
    menu = "┌" + "─" * (large + 1) + "┐\n"
    centre = (large - len(title)) / 2
    menu += "│" + " " + Fore.YELLOW + title + Fore.RESET + " " * (large - len(title)) + "│\n"
    menu += "├" + "─" * (large + 1) + "┤\n"

    # Generar opciones
    cont = 1
    large += 1
    for i in options:
        menu += f"│ {Fore.GREEN}{cont}{Fore.RESET} -> {i} {" " * (large - len(i) - 8)} │\n"
        cont += 1

    # Generar final
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
    tel1 = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el primer teléfono del usuario: ")
    tel2 = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte el segundo teléfono del usuario: ")
    direccion = input(f"{Fore.MAGENTA}[+]{Fore.RESET} Inserte la dirección del usuario: ")

    writecsv([nombre, apellido, tel1, tel2, direccion])
    return 0

def modificarDatos():
    return 0

def darBaja():
    return 0

def buscarDato():
    return 0

def mostrarDato():
    datos = readcsv()
    line = "╔"
    for upper in datos[0]:
        line += "═" * (len(upper) + 2)
        line += "╦"
    line = line[:-1] + "╗"
    print(line)
    line = "║"
    for title in datos[0]:
        line += " " + title + " ║"
    print(line)
    line = "╠"
    for upper in datos[0]:
        line += "═" * (len(upper) + 2)
        line += "╬"
    line = line[:-1] + "╣"
    print(line)
    return 0

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
            exit()