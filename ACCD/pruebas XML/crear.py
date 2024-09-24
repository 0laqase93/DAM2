import xml.etree.ElementTree as ET
from xml.dom import minidom

# Crear la estructura del archivo
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item3 = ET.SubElement(items, 'item')
item1.set('name', 'manolo1')
item2.set('name', 'manolo2')
item3.set('name', 'manolo3')
item1.text = 'item1abc'
item2.text = 'item2abc'
item3.text = 'item3abc'

# Crear un nuevo archivo XML con los resultados
tree = ET.ElementTree(data)

# Convertir el árbol a una cadena y formatearlo
xml_str = ET.tostring(data, encoding='utf-8', method='xml')
parsed_xml = minidom.parseString(xml_str)
pretty_xml_str = parsed_xml.toprettyxml()

# Escribir el XML formateado en un archivo
with open('data.xml', 'w', encoding='utf-8') as f:
    f.write(pretty_xml_str)

print("XML creado")