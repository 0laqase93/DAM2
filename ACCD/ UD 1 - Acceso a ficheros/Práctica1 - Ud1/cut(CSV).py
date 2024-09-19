import csv

valores = ''
with open("listado-codigos-postales.csv", encoding = "utf-8", newline = '') as csvfile:
    delimiter = csv.Sniffer().sniff(csvfile.readline()).delimiter
    csvfile.seek(0)
    data = csv.reader(csvfile, delimiter = delimiter)
    valores = list(data)
    print(valores)

