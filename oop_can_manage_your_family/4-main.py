from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family = load_from_file("my_family.json")
i = len(my_family) + 1
m = Adult(i, "Marc", [7, 4, 1990], "Male", "Green")
my_family.append(m)
i += 1
v = Adult(i, "Vaness", [7, 4, 1992], "Female", "Green")
my_family.append(v)

if m.is_married():
    print "Marc is married"
else:
	print "Marc isn't married"

m.just_married_with(v)
if m.is_married():
    print "Marc is NOW married"

save_to_file(my_family, "my_family.json")
