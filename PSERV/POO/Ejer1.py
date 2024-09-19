"""
Escribir una clase en python que convierta un número entero a número romano
"""

class NumeroRomano:
    def __init__(self, numero):
        self.numero = numero
        self.romano = self.convertir_a_romano()

    def convertir_a_romano(self):
        values = {
            1000:'M', 900:'CM', 500:'D',
            400:'CD', 100:'C', 90:'XC',
            50:'L', 40:'XL', 10:'X',
            9:'IX', 5:'V', 4:'IV',
            1:'I'
        }

        resultado = ''
        numero = self.numero
        for value, simbolo in values.items():
            while numero >= value:
                resultado += simbolo
                numero -= value
        return resultado

    def __str__(self):
        return f"{self.numero} en números romanos es {self.romano}"

numero = NumeroRomano(800)
print(numero)
