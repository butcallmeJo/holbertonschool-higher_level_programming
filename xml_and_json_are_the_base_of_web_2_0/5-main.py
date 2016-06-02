from car import Car
import json
import xml.dom.minidom as minidom

with open("5-main.json") as f:
	list_cars_json = json.load(f)

cars = []
brands = []
for car in list_cars_json:
	name2 = car['name']
	brand2 = car['brand']
	nb_doors2 = car['nb_doors']
	cars.append(Car(name=str(name2), brand=str(brand2), nb_doors=int(nb_doors2)))

total_nb_doors = 0
for car in cars:
	if car.get_brand() not in brands:
		brands.append(car.get_brand())
	total_nb_doors += car.get_nb_doors()

print len(brands)
print total_nb_doors
print cars[3]

xmlstr = '<cars>\n</cars>\n'
doc = minidom.parseString(xmlstr)
for car in cars:
	doc.getElementsByTagName('cars')[0].appendChild(car.to_xml_node(doc))

print doc.toxml(encoding='utf-8')
