import xml.etree.ElementTree as ET
import os
from html.parser import charref

from colorama import init, Fore
init()

ARCHIVO_XML = 'agenda.xml'

def guardarDatos():
    try:
        tree = ET.parse(ARCHIVO_XML)
        agenda = tree.getroot()
    except:
        agenda = ET.Element(ARCHIVO_XML)

    contacto = ET.SubElement(agenda, 'contacto')

    nombre = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el nombre del usuario: ")
    apellido = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el apellido del usuario: ")
    email = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el email del usuario: ")
    tel1 = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el primer teléfono del usuario: ")
    tel2 = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el segundo teléfono del usuario (opcional): ")
    direccion = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte la dirección del usuario: ")


    ET.SubElement(contacto, 'nombre').text = nombre
    ET.SubElement(contacto, 'apellido').text = apellido
    ET.SubElement(contacto, 'email').text = email
    ET.SubElement(contacto, 'telefono1').text = tel1
    ET.SubElement(contacto, 'telefono2').text = tel2
    ET.SubElement(contacto, 'direccion').text = direccion

    tree = ET.ElementTree(agenda)
    tree.write(ARCHIVO_XML)

    print(f"{Fore.GREEN}[+]{Fore.RESET} Contacto guardado con éxito.")
    print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
    input()

def mostrarMenu():
    os.system('cls' if os.name == 'nt' else 'clear')

    opciones = [
        "Guardar datos",
        "Modificar datos",
        "Dar de baja",
        "Buscar",
        "Mostrar",
        "Salir"
    ]

    contador = 1
    for opcion in opciones:
        print(f"{Fore.GREEN}{contador}{Fore.RESET} -> {opcion}")
        contador += 1

def mostrar():
    try:
        tree = ET.parse(ARCHIVO_XML)
        agenda = tree.getroot()
    except:
        print(f"{Fore.RED}[-]{Fore.RESET} No hay contactos para mostrar.")
        print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
        input()
        return


    print("-----")
    for contacto in agenda.findall('contacto'):
        nombre = contacto.find('nombre').text
        apellido = contacto.find('apellido').text
        email = contacto.find('email').text
        telefono1 = contacto.find('telefono1').text
        telefono2 = contacto.find('telefono2').text
        direccion = contacto.find('direccion').text

        print(f"{Fore.GREEN}[+] {Fore.RESET}{nombre} {apellido}{Fore.GREEN}:{Fore.RESET}")
        print(f"\t {Fore.BLUE}email:{Fore.RESET} {email}")
        print(f"\t {Fore.BLUE}telefono1:{Fore.RESET} {telefono1}")
        print(f"\t {Fore.BLUE}telefono2:{Fore.RESET} {telefono2}")
        print(f"\t {Fore.BLUE}direccion:{Fore.RESET} {direccion}")
        print("-----")

    print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
    input()

def modificarDatos():
    try:
        tree = ET.parse(ARCHIVO_XML)
        agenda = tree.getroot()
    except FileNotFoundError:
        print(f"{Fore.RED}[-]{Fore.RESET} No se encontró el archivo {ARCHIVO_XML}.")
        print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
        input()
        return

    encontrado = False
    inputBuscado = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el nombre o apellido del contacto a modificar: ")

    for contacto in agenda.findall('contacto'):
        nombreEncontrado = contacto.find('nombre').text
        apellidoEncotrado = contacto.find('apellido').text
        
        if inputBuscado.lower() == nombreEncontrado.lower() or inputBuscado.lower() == apellidoEncotrado.lower():
            encontrado = True

            nuevo_nombre = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el nuevo nombre: ") or contacto.find('nombre').text
            nuevo_apellido = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el nuevo apellido: ") or contacto.find('apellido').text
            nuevo_email = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el nuevo email: ") or contacto.find('email').text
            nuevo_tel1 = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el nuevo primer teléfono: ") or contacto.find('telefono1').text
            nuevo_tel2 = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el nuevo segundo teléfono: ") or contacto.find('telefono2').text
            nueva_direccion = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte la nueva dirección: ") or contacto.find('direccion').text

            contacto.find('nombre').text = nuevo_nombre
            contacto.find('apellido').text = nuevo_apellido
            contacto.find('email').text = nuevo_email
            contacto.find('telefono1').text = nuevo_tel1
            contacto.find('telefono2').text = nuevo_tel2
            contacto.find('direccion').text = nueva_direccion

            tree.write(ARCHIVO_XML)
            print(f"{Fore.GREEN}[+]{Fore.RESET} Contacto modificado con éxito.")

    if not encontrado:
        print(f"{Fore.RED}[-]{Fore.RESET} Contacto no encontrado.")
    print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
    input()

def darDeBaja():
    tree = ET.parse(ARCHIVO_XML)
    agenda = tree.getroot()

    try:
        criterio = input(f"{Fore.GREEN}[?]{Fore.RESET} Ingrese el nombre o apellido del contacto a eliminar: ").lower()
        encontrados = []

        for contacto in agenda.findall('contacto'):
            nombre = contacto.find('nombre').text.lower()
            apellido = contacto.find('apellido').text.lower()

            if criterio in nombre or criterio in apellido:
                encontrados.append(contacto)
                print(f"{Fore.YELLOW}Contacto encontrado: {nombre.title()} {apellido.title()}{Fore.RESET}")

        if not encontrados:
            print(f"{Fore.RED}[+]{Fore.RESET} No se encontraron contactos con ese criterio.")
            return

        opcion = input(f"{Fore.GREEN}[?]{Fore.RESET} ¿Desea borrar estos contactos? S/n: ").lower()

        if opcion == 's' or opcion == '':
            for contacto in encontrados:
                agenda.remove(contacto)
            tree.write(ARCHIVO_XML)
            print(f"{Fore.BLUE}[+]{Fore.RESET} Contacto(s) eliminado(s) exitosamente.")
        elif opcion == 'n':
            print(f"{Fore.RED}[+]{Fore.RESET} Operación cancelada.")
        else:
            raise Exception("Opción inválida")

    except Exception as e:
        print(f"{Fore.RED}[-]{Fore.RESET} Error: {str(e)}")

    finally:
        print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
        input()

def buscar():
    try:
        tree = ET.parse(ARCHIVO_XML)
        agenda = tree.getroot()
    except:
        print(f"{Fore.RED}[!]{Fore.RESET} Archivo no encontrado.")
        print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
        input()
        return

    inputBuscado = input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte el nombre o apellido del contacto a buscar: ")
    encontrado = False

    for contacto in agenda.findall('contacto'):
        nombreEncontrado = contacto.find('nombre').text
        apellidoEncotrado = contacto.find('apellido').text

        if inputBuscado.lower() == nombreEncontrado.lower() or inputBuscado.lower() == apellidoEncotrado.lower():
            encontrado = True

            nombre = contacto.find('nombre').text
            apellido = contacto.find('apellido').text
            email = contacto.find('email').text
            tel1 = contacto.find('telefono1').text
            tel2 = contacto.find('telefono2').text
            direccion = contacto.find('direccion').text

            print("-----")
            print(f"{Fore.GREEN}[+] {Fore.RESET}{nombre} {apellido}{Fore.GREEN}:{Fore.RESET}")
            print(f"\t {Fore.BLUE}email:{Fore.RESET} {email}")
            print(f"\t {Fore.BLUE}telefono1:{Fore.RESET} {tel1}")
            print(f"\t {Fore.BLUE}telefono2:{Fore.RESET} {tel2}")
            print(f"\t {Fore.BLUE}direccion:{Fore.RESET} {direccion}")
            print("-----")

    if not encontrado:
        print(f"{Fore.RED}[-]{Fore.RESET} Contacto no encontrado.")

    print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
    input()

# AQUÍ EMPIEZA EL PROGRAMA
option = -1
while option != 6:
    mostrarMenu()
    try:
        option = int(input(f"{Fore.GREEN}[+]{Fore.RESET} Inserte su opción: "))
        match option:
            case 1:
                guardarDatos()
            case 2:
                modificarDatos()
            case 3:
                darDeBaja()
            case 4:
                buscar()
            case 5:
                mostrar()
            case 6:
                continue
            case default:
                print(f"{Fore.RED}[!] Opción no válida.{Fore.RESET}")
                print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
                input()
    except ValueError:
        print(f"{Fore.RED}[!]{Fore.RESET} Solo se pueden escribir números enteros.{Fore.RESET}")
        print(f"{Fore.MAGENTA}[+] Presione enter para continuar...{Fore.RESET}", end="")
        input()


print(f"{Fore.RED}[+] Saliendo del programa...{Fore.RESET}")