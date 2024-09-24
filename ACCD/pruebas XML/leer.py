import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

# Leer el primer elemento
for elem in root:
    print(elem.find('item').get('name') + " : " + elem.find('item').text)

# Leer un elemento en el que sabemos el nombre de un atributo
elem2 = root.find(".//item[@name='manolo3']")
print(elem2.get('name') + " : " + elem2.text)