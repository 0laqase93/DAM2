"""
Escriba un programa que pida dos números y que escriba su media aritmética.
"""

from colorama import init, Fore
init()

var1 = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte un número: "))
var2 = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte otro número: "))
media = (var1 + var2) / 2

print("La media es: " + Fore.RED, str(media))