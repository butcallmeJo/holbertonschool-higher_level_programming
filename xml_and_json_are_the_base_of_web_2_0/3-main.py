from car import Car

c = Car(name="Rogue", brand="Nissan", nb_doors=5)
print "c: %s" % c

c2 = Car(c)
c2.set_nb_doors(3)
print "c2: %s" % c2
print "c: %s" % c
