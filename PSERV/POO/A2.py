"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuentaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular
y la cantidad se debe guardar una bonificación que estará expresada en porcentaje.
Construye los siguientes métodos para la clase:
    • Constructor.
    • Los setters y getters para el nuevo atributo.
    • Los titulares de este tipo de cuenta tienen que ser mayor de edad y menor de 25 años.
        Hay que crear un método esTitularValido() que devuelve true si el titular es mayor de
        edad pero menor de 25 años y false en caso contrario.
    • La retirada de dinero sólo se podrá hacer si el titular es válido.
    • El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de
        la cuenta.
Piensa los métodos heredados de la clase superior que hay que reescribir.
"""

from A1 import Cuenta
from Ejer4 import Persona

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        self.titular = titular
        self.cantidad = cantidad
        self.bonificacion = bonificacion

    def getBonificacion(self):
        return self.bonificacion

    def setBonificacion(self, bonificacion):
        if 0 <= bonificacion <= 100 :
            self.bonificacion = bonificacion
        else:
            print("[!] La bonificación no puede ser menor a 0 y mayor a 100.")

    def esTitularValido(self):
        edad = int(self.titular.getEdad())
        if 18 <= edad < 25:
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("[+] No cumple el requisito de tener en tre 18 y 25 años.")

    def mostrar(self):
        print(self.createMenu([
            "Cuenta Joven",
            "------------",
            "Titular: " + str(self.titular),
            "Cantidad: " + str(self.cantidad) + " €",
            "Bonificacion: " + str(self.bonificacion) + "%"
        ]))