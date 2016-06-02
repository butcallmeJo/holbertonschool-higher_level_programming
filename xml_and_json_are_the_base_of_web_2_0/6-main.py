from car import Car
import json
import xml.dom.minidom as minidom

with open("6-main.json") as f:
	list_cars_json = json.load(f)

cars = []
my_list = []
for car in list_cars_json:
	name2 = car['name']
	brand2 = car['brand']
	nb_doors2 = car['nb_doors']
	cars.append(Car(name=str(name2), brand=str(brand2), nb_doors=int(nb_doors2)))

total_nb_doors = 0
for car in cars:
	my_list.append(car.to_comma())

print "\n".join(my_list)
