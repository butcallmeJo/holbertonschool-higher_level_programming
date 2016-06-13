import sys
import peewee
from models import *

action_list = ["create", "print", "insert", "delete"]
table_list = ["school", "batch", "student"]
models = {
	'school': School,
	'batch': Batch,
	'user': User,
	'student': Student
}

def print_table(table):
	for table in table.select():
		print table

def insert_model():
	if sys.argv[2] == "school":
		if len(sys.argv) != 4 or not isinstance(sys.argv[3], str):
			print "error: insert school usage: insert school <name>"
		else:
			obj = School.create(name=sys.argv[3])
	elif sys.argv[2] == "batch":
		if len(sys.argv) != 5:
			print "error: insert batch usage: insert batch <school id> <name>"
		else:
			obj = Batch.create(school=sys.argv[3], name=sys.argv[4])
	elif sys.argv[2] == "student":
		if len(sys.argv) == 7:
			obj = Student.create(
				batch=sys.argv[3],
				age=sys.argv[4],
				last_name=sys.argv[5],
				first_name=sys.argv[6]
			)
		elif len(sys.argv) == 6:
			obj = Student.create(
				batch=sys.argv[3],
				age=sys.argv[4],
				last_name=sys.argv[5],
			)
		else:
			print "error: insert batch usage: insert batch <school id> <name>"

	print "New " + sys.argv[2] + ": ", obj

def delete_obj():
	try:
		table = models[sys.argv[2]]
		obj = table.get(id=sys.argv[3])
		obj.delete_instance()
		print "Delete: ", obj
	except:
		print "Nothing to delete"


#
if len(sys.argv) < 2:
	print "Please enter an action"
#
elif len(sys.argv) > 1 and sys.argv[1] not in action_list:
	print "Undefined action " + str(sys.sys.argv[1])
#
elif sys.argv[1] == "create":
	my_models_db.connect()
	my_models_db.create_tables([BaseModel, School, Batch, User, Student])
#
elif sys.argv[1] == "print":
	if len(sys.argv) < 3:
		print "error: print needs one argument"
	elif sys.argv[2] not in table_list:
		print "error: " + sys.argv[2] + " not in table"
	else:
		if sys.argv[2] == "school":
			print_table(School)
		elif sys.argv[2] == "batch":
			print_table(Batch)
		elif sys.argv[2] == "student":
			print_table(Student)
#
elif sys.argv[1] == "insert":
	if len(sys.argv) < 3:
		print "error: insert needs at least one argument"
	elif sys.argv[2] not in table_list:
		print "error: " + sys.argv[2] + " not in table"
	else:
		insert_model()
#
elif sys.argv[1] == "delete":
	if len(sys.argv) != 4:
		print "error: delete usage: <tabel_name> <object_id>"
	elif sys.argv[2] not in table_list:
		print "error: " + sys.argv[2] + " not in table"
	else:
		delete_obj()
