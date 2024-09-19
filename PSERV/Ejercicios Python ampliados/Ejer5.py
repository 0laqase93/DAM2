"""
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla los datos.
"""

year = int(input("[+] Ingrese el año en curso: "))

try:
    people = {
        input("[+] Introduzca el nombre 1: "): int(input("[+] Introduzca el año de nacimiento 1: ")),
        input("[+] Introduzca el nombre 2: "): int(input("[+] Introduzca el año de nacimiento 2: ")),
        input("[+] Introduzca el nombre 3: "): int(input("[+] Introduzca el año de nacimiento 3: "))
    }

    for nombre, anyo in people.items():
        print(f"Nombre: {nombre} - Fecha de nacimiento {anyo} - Cumplirá {year - anyo} años.")
except ValueError:
    print("[!] Error en el cálculo.")
