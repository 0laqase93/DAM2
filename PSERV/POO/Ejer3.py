"""
Escribir una clase en python con los siguientes métodos:
    1- get_string. acepta una cadena introducida por el usuario
    2- print_string. imprime la cadena en mayúsculas.
    3- rev_string. invierte una cadena por palabras
        Entrada: "Mi Diario Python"
        Salida: "Python Diario Mi"
"""

class Clase:
    def __init__(self):
        self.texto = ""

    def get_string(self, texto):
        self.texto = texto

    def print_string(self):
        print(self.texto.upper())

    def rev_string(self):
        self.texto = self.texto[::-1]
        return self.texto

clase = Clase()
clase.get_string("Mi Diario Python")
clase.print_string()
print(clase.rev_string())
