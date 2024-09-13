"""
Escriba un programa que pida primero un número par (positivo o negativo) y si
el valor no es correcto, muestre un aviso. Si el valor es correcto, pedirá un número
impar (positivo o negativo) y si el valor no es correcto, mostrará un aviso.
"""

from colorama import init, Fore
init()

par = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte un numero " + Fore.GREEN + "PAR" + Fore.RESET + ": "))

if par % 2 == 0:
    impar = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte un numero " + Fore.GREEN + "IMPAR" + Fore.RESET + ": "))
    if impar % 2 == 1:
        print(Fore.GREEN + "[+]" + Fore.RESET + " ¡¡Has insertado los datos con éxito!!")
    else:
        print(Fore.RED + "[+]" + Fore.RESET + " No es un número impar :(")
else:
    print(Fore.RED + "[+]" + Fore.RESET + " No es un número par :(")