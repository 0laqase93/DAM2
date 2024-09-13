archivo = open("archivo2.txt", 'a')

archivo.write("\nHola jaja saludos 3")

archivo = open("archivo2.txt", "r")

amarilloConNegrita = chr(27)+"[1;33m"
blancoNormal = chr(27)+"[0;37m"
linea = archivo.readline()
numlinea = 0
while linea != "":
    numlinea += 1
    print(amarilloConNegrita, numlinea, blancoNormal, linea, end = "")
    linea = archivo.readline()
archivo.close()