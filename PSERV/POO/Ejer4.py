"""
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye
los siguientes métodos para la clase:
    •Un constructor, donde los datos pueden estar vacíos.
    •Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
    datos.
    •mostrar(): Muestra los datos de la persona.
    •esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

import re

class Persona:
    def __init__(self, nombre = "Nombre", edad = 0, dni = "13245678A"):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setDni(dni)

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getDni(self):
        return self.dni

    def setNombre(self, nombre):
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            print("[!] El nombre tiene que ser una cadena de texto.")

    def setEdad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("[!] La edad no puede ser menor a 0.")

    def setDni(self, dni):
        patronDni = r'^\d{8}[A-Z]$'
        if isinstance(dni, str):
            if re.match(patronDni, dni):
                self.dni = dni
            else:
                print("[!] El DNI no tiene un formato valido.")
        else:
            print("[!] El nombre tiene que ser una cadena de texto.")

    def mostrar(self):
        print(self.createMenu([
            "Nombre: " + self.nombre,
            "Edad: " + str(self.edad),
            "Dni: " + self.dni
        ]))

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        return False

    def createMenu(self, options):
        large = 0
        for i in options:
            if large < len(i) + 2:
                large = len(i) + 2

        # Generar opciones
        menu = "┌" + "─" * (large + 1) + "┐\n"
        cont = 1
        large += 1
        for i in options:
            menu += f"│ {i} {" " * (large - len(i) - 3)} │\n"
            cont += 1

        # Generar final
        menu += "└" + "─" * large + "┘"

        return menu

    def __str__(self):
        return self.nombre