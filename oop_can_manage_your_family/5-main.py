from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family = load_from_file("my_family.json")

marc = my_family[0]
vanessa = my_family[1]
boby = my_family[2]

vanessa.adopt_child(boby)
marc.adopt_child(boby)
hyuna = vanessa.has_child_with(marc, 7, "Hyuna", [4, 2, 2011], "Female", "Brown")
my_family.append(hyuna)
print "Vanessa has %d children" % (len(vanessa.children))

save_to_file(my_family, "my_family.json")
