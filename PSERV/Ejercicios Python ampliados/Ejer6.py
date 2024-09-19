"""
Definir un diccionario con los nombres y las edades de 10 personas. Imprimir una lista con los
nombres de las personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

personas = {
    "Ana": 0,
    "Luis": 0,
    "Carlos": 0,
    "María": 0,
    "Jorge": 0,
    "Lucía": 0,
    "Pedro": 0,
    "Elena": 0,
    "Raúl": 0,
    "Sofía": 0
}

for nombre, edad in personas.items():
    try:
        personas[nombre] = int(input(f"[+] Ingrese la edad de la persona {nombre}: "))
    except ValueError:
        print("[!] Error en la edad.")


print("[+] Las personas mayores de 20 años son:")
for nombre, edad in personas.items():
    if edad > 20:
        print(f"-> {nombre}")
