"""
Escribir una clase en python que encuentre un par de elementos (índice de los números) de
una matriz dada cuya suma es igual a un número de destino específico.
"""


class Pares:
    def __init__(self, lista, objetivo):
        self.lista = lista
        self.objetivo = objetivo

    def buscar_pares(self):
        indexados = list(enumerate(self.lista))
        indexados.sort(key=lambda x: x[1])

        inicio = 0
        fin = len(indexados) - 1

        while inicio < fin:
            suma = indexados[inicio][1] + indexados[fin][1]
            if suma == self.objetivo:
                return (indexados[inicio][0] + 1, indexados[fin][0] + 1)
            elif suma < self.objetivo:
                inicio += 1
            else:
                fin -= 1

        return None

pares = Pares([10, 20, 10, 40, 50, 60, 70], 50)
resultado = pares.buscar_pares()

if resultado:
    print(f"Los índices que suman {pares.objetivo} son: {resultado}")
else:
    print(f"No se encontraron pares que sumen {pares.objetivo}.")
