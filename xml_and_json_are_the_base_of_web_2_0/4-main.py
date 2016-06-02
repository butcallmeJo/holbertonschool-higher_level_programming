from car import Car
import json
from xml.dom.minidom import getDOMImplementation, Document

c = Car(name="Rogue", brand="Nissan", nb_doors=5)
print c
c_json_string = c.to_json_string()
print type(c_json_string)
print c_json_string

doc = Document()
'''Comment the next two lines for testing puposes'''
c_xml = c.to_xml_node(doc)
doc.appendChild(c_xml)

print doc.toxml(encoding='utf-8')


'''The following to use for test puposes'''
# car = doc.createElement('car')
# car.setAttribute('nb_doors', "5")
# name = doc.createElement('name')
# name_content = doc.createTextNode("rogue")
# brand = doc.createElement('name')
# brand_content = doc.createTextNode("nissan")
# name.appendChild(name_content)
# brand.appendChild(brand_content)
# car.appendChild(name)
# car.appendChild(brand)
# doc.appendChild(car)
