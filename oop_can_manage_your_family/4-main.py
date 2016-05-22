from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family = load_from_file("my_family.json")
i = len(my_family) + 1
m = Adult(i, "Marc", [7, 4, 1990], "Male", "Green")
m.last_name = "Lardi"
i += 1
v = Adult(i, "Vanessa", [7, 4, 1992], "Female", "Green")
v.last_name = "Idral"

if m.is_married():
    print "Marc is married"
else:
	print "Marc isn't married"

v.just_married_with(m)
if m.is_married():
    print "Marc is NOW married"

my_family.append(m)
my_family.append(v)


save_to_file(my_family, "my_family.json")
