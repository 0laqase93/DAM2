"""
Crear una función contar_vocales(), que permita escribir una frase y cuente cuántas letras "a"
tiene, cuántas letras "e" tiene ... Y así hasta completar todas las vocales.
"""
from itertools import count


def contar_vocales(frase):
    vocales = [0, 0, 0, 0, 0]

    for letra in frase:
        match letra.lower():
            case 'a':
                vocales[0] += 1
            case 'e':
                vocales[1] += 1
            case 'i':
                vocales[2] += 1
            case 'o':
                vocales[3] += 1
            case 'u':
                vocales[4] += 1
    print(f"[+] {frase} tiene:\n A = {vocales[0]}\n E = {vocales[1]}\n I = {vocales[2]}\n O = {vocales[3]}\n U = {vocales[4]}")

def contar_vocales2(frase):
    vocales = ['a', 'e', 'i', 'o', 'u']
    print(f"[+] {frase} tiene:")
    for letra in vocales:
        print(f" {letra} = {frase.count(letra)}")


#contar_vocales('Hola Diego eres un poco lento :)')
contar_vocales2('Hola Diego eres un poco lento :)')