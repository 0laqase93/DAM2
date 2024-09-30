from A1 import *

persona = Persona("Jose Jacinto Segundo", 23, "12345678A")
cuenta = Cuenta(persona, 500)
cuenta.mostrar()
cuenta.ingresar(10)
cuenta.mostrar()
cuenta.retirar(50)
cuenta.mostrar()