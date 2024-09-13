"""
Escriba un programa que pida dos números enteros y escriba los números pares
entre ellos dos, desde el menor hasta el mayor.
"""

from colorama import init, Fore
init()

var1 = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte el primer valor: "))
var2 = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte el segundo valor: "))

var1 += var1 % 2
var2 -= var2 % 2

print(list(range(var1, var2 + 1, 2)))