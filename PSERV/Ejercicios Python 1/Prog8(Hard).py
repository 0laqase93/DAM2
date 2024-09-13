"""
Escriba un programa que permita crear una lista de palabras y que, a
continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
"""

from colorama import init, Fore
init()

list = []
size = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte el tamaño de la lista: "))

for i in range(size):
    list.append(input(Fore.MAGENTA + str(i + 1) + Fore.RESET + Fore.YELLOW + " [+]" + Fore.RESET + " Inserte una palabra: "))

word = input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte la palabra que quiere contar: ")
set = set(list)
times = len(list) - len(set) + 1
if word not in list:
    times -= 1
print(f'{Fore.YELLOW}[+]{Fore.RESET} La palabra {Fore.BLUE}{word}{Fore.RESET} aparece un total de {Fore.GREEN}{times}{Fore.RESET} veces repetidas')
