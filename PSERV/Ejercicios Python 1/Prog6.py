"""
Escriba un programa que pida un número entero mayor que cero y que escriba
sus divisores.
(Optimiza el programa teniendo en cuenta que los divisores son siempre menores o
iguales que la mitad del número).
"""

from colorama import init, Fore
init()

var = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte un número mayor que cero: "))

print(Fore.GREEN + "[+]" + Fore.RESET + " Los divisores de " + Fore.BLUE + str(var) + Fore.RESET + " son:", end=" ")
for i in range(1, var // 2 + 1):
    if var % i == 0:
        print(Fore.GREEN + str(i), end=" ")