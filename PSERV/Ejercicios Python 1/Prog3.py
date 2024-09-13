"""
Escriba un programa que pida primero un número par y luego un número impar
(positivos o negativos). En caso de que uno o los dos valores no sea correcto, se
mostrará un único aviso.
"""

from colorama import init, Fore
init()

par = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte un numero " + Fore.GREEN + "PAR" + Fore.RESET + ": "))
impar = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte un numero " + Fore.GREEN + "IMPAR" + Fore.RESET + ": "))

if par % 2 == 0 and impar % 2 != 0:
    print(Fore.GREEN + "[+]" + Fore.RESET + " ¡¡Has insertado los datos con éxito!!")
else:
    print(Fore.RED + "[+]" + Fore.RESET + " Uno o los dos valores no son correctos :(")