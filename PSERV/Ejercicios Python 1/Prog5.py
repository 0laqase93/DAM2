"""
Escriba un programa que pida dos números enteros y escriba los números pares
entre ellos dos, desde el menor hasta el mayor.
"""

from colorama import init, Fore
init()

var1 = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte el primer valor: "))
var2 = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte el segundo valor: "))

print(Fore.GREEN + "[+]" + Fore.RESET + " Los número pares entre el " + Fore.BLUE + str(var1) + Fore.RESET + " y el " + Fore.BLUE + str(var2) + Fore.RESET + " son:", end=" " )
for i in range(var1, var2 + 1):
    if i % 2 == 0:
        print(Fore.GREEN + str(i), end=" ")