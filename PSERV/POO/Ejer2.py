"""
Escribir una clase en python que encuentre un par de elementos (índice de los números) de
una matriz dada cuya suma es igual a un número de destino específico.
"""

class Pares:
    lista = []
    objetivo = 0
    def __init__(self, lista, objetivo):
        self.lista = lista
        self.objetivo = objetivo
        self.buscarPares()

    def encontrar_indices(self):
        index = list(enumerate(self.lista))
        index = filter(lambda x: x[1] == self.objetivo, index)
        index = sorted(index, key=lambda x: x[1])


pares = Pares([10,20,10,40,50,60,70], 50)

print(pares)