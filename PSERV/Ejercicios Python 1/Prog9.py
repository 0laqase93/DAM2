"""
Implementar alguno de los programas anteriores en funciones y organizar el
código. Se propone el Prog5 y Prog6.
"""

from colorama import init, Fore
init()

def prog5():
    print("-----")
    print(Fore.RED + "Prog5" + Fore.RESET)
    print("-----")
    var1 = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte el primer valor: "))
    var2 = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte el segundo valor: "))

    print(Fore.GREEN + "[+]" + Fore.RESET + " Los número pares entre el " + Fore.BLUE + str(
        var1) + Fore.RESET + " y el " + Fore.BLUE + str(var2) + Fore.RESET + " son:", end=" ")
    for i in range(var1, var2 + 1):
        if i % 2 == 0:
            print(Fore.GREEN + str(i), end=" ")
    print(Fore.RESET)

def prog6():
    print("-----")
    print(Fore.RED + "Prog6" + Fore.RESET)
    print("-----")
    var = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte un número mayor que cero: "))

    print(Fore.GREEN + "[+]" + Fore.RESET + " Los divisores de " + Fore.BLUE + str(var) + Fore.RESET + " son:", end=" ")
    for i in range(1, var // 2 + 1):
        if var % i == 0:
            print(Fore.GREEN + str(i), end=" ")
    print(Fore.RESET)

prog5()
prog6()