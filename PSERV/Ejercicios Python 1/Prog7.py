"""
Escriba un programa que permita crear una lista de palabras. Para ello, el
programa tiene que pedir un número y luego solicitar ese número de palabras para
crear la lista. Por último, el programa tiene que escribir la lista.
"""

from colorama import init, Fore
init()

list = []
size = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte el tamaño de la lista: "))

for i in range(size):
    list.append(input(Fore.MAGENTA + str(i + 1) + Fore.RESET + Fore.YELLOW + " [+]" + Fore.RESET + " Inserte una palabra: "))

print(list)