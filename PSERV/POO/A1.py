"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Construye los siguientes métodos para la clase:
    • Un constructor, donde los datos pueden estar vacíos.
    • Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
      directamente, sólo ingresando o retirando dinero.
    • mostrar(): Muestra los datos de la cuenta.
    • ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
      negativa, no se hará nada.
    • retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
      números rojos.
"""

from Ejer4 import Persona

class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = float(cantidad) # La cantidad se maneja en céntimos

    def getTitular(self):
        return self.titular

    def getCantidad(self):
        return self.cantidad / 100

    def setTitular(self, titular):
        self.titular = titular

    def mostrar(self):
        print(self.createMenu([
            "Titular: " + str(self.titular),
            "Cantidad: " + str(self.cantidad) + " €"
        ]))

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

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("[!] No se puede ingresar cantidad negativa ni 0€.")

    def retirar(self, cantidad):
        if self.cantidad - cantidad >= 0:
            self.cantidad -= cantidad
        else:
            self.cantidad -= cantidad
            print("[!] Cantidad en la cuenta en números rojos.")