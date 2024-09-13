"""
Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de
una persona y que calcule su índice de masa corporal (imc). (imc = peso / altura²).
"""

from colorama import init, Fore
init()

peso = int(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte su peso en kilogramos: "))
altura = float(input(Fore.YELLOW + "[+]" + Fore.RESET + " Inserte su altura en metros: "))
print(f'{Fore.GREEN}[+]{Fore.RESET} Su IMC es igual a {Fore.BLUE}{peso / altura**2:.2f}')