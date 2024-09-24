import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('data.xml')
root = tree.getroot()

# adding an element to the root node
atrib = {}
element = root.makeelement('seconditems', atrib)
root.append(element)

# adding an element to the seconditems node
attrib = {'name2': 'secondname2'}
subelement = root[0][1].makeelement('seconditem', attrib)
ET.SubElement(root[1], 'seconditem', attrib)
root[1][0].text = 'seconditemabc'

xml_str = ET.tostring(root, encoding='utf-8', method='xml')
parsed_xml = minidom.parseString(xml_str)
pretty_xml_str = parsed_xml.toprettyxml()

# create a new XML file with the new element
tree.write('newitems2.xml')