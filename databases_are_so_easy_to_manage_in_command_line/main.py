import sys
import peewee
from models import *
from actions import *

action_list = ["create", "print", "insert", "delete", "print_batch_by_school", "print_student_by_batch", "print_student_by_school", "print_family", "age_average", "change_batch", "print_all"]
table_list = ["school", "batch", "student"]
models = {
	'school': School,
	'batch': Batch,
	'user': User,
	'student': Student
}

#
def print_all():
	for school in School.select():
		print school
		for batch in school.batches:
			print "\t", batch
			for student in batch.students:
				print "\t\t", student

#
def change_batch():
	try: student = Student.get(id=sys.argv[2])
	except: print 'Student not found'; return

	try: batch = Batch.get(id=sys.argv[3])
	except: print 'Batch not found'; return

	if student.batch == batch:
		print student, "already in", batch
	else:
		print student, "has been moved to", batch
		student.batch = sys.argv[3]
		student.save()

#
def age_average():
	age_avg = 0
	if len(sys.argv) == 3:
		batch_id = sys.argv[2]
		for obj in Student.select().where(Student.batch==batch_id):
			age_avg += obj.age
		print age_avg
	else:
		for obj in Student.select():
			age_avg += obj.age
		print age_avg

#
def print_family(student_last_name):
	try:
		Student.get(last_name=student_last_name)
		for obj in Student.select().where(Student.last_name==student_last_name):
			print obj
	except:
		print "Last name not found"
#
def print_student_by_school(school_id):
	n = 0
	for obj in Student.select().join(Batch).where(Batch.school==school_id):
		print obj
		n += 1
	if n == 0: print "School not found"

#
def print_student_by_batch():
	n = 0
	batch_id = sys.argv[2]
	for obj in Student.select().where(Student.batch==batch_id):
		print obj
		n += 1
	if n == 0: print "Batch not found"

#
def print_batch_by_school(school_id):
	n = 0
	for obj in Batch.select().where(Batch.school==school_id):
		print obj
		n += 1
	if n == 0: print "School not found"

#
def print_table(table):
	for table in table.select():
		print table

#
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

#
def delete_obj():
	try:
		table = models[sys.argv[2]]
		obj = table.get(id=sys.argv[3])
		obj.delete_instance()
		print "Delete: ", obj
	except:
		print "Nothing to delete"


'''=============================='''
'''|| MAIN PROGRAM STARTS HERE ||'''
'''=============================='''

#
if len(sys.argv) < 2:
	print "Please enter an action"
#
elif len(sys.argv) > 1 and sys.argv[1] not in action_list:
	print "Undefined action " + str(sys.argv[1])
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
		print "error: delete usage: <table_name> <object_id>"
	elif sys.argv[2] not in table_list:
		print "error: " + sys.argv[2] + " not in table"
	else:
		delete_obj()
#
elif sys.argv[1] == "print_batch_by_school":
	if len(sys.argv) != 3:
		print "error: print_batch_by_school usage: <school id>"
	else:
		print_batch_by_school(sys.argv[2])
#
elif sys.argv[1] == "print_student_by_batch":
	if len(sys.argv) != 3:
		print "error: print_student_by_batch usage: <batch id>"
	else:
		print_student_by_batch(sys.argv[2])
#
elif sys.argv[1] == "print_student_by_school":
	if len(sys.argv) != 3:
		print "error: print_student_by_school usage: <school id>"
	else:
		print_student_by_school(sys.argv[2])
#
elif sys.argv[1] == "print_family":
	if len(sys.argv) != 3:
		print "error: print_family usage: <last_name>"
	else:
		print_family(sys.argv[2])
#
elif sys.argv[1] == "age_average":
	if len(sys.argv) != 3 and len(sys.argv) != 2:
		print "error: age_average usage: (optional: <batch id>)"
	else:
		age_average()
#
elif sys.argv[1] == "change_batch":
	if len(sys.argv) != 4:
		print "error: change_batch usage: <student id> <batch id>"
	else:
		change_batch()
#
elif sys.argv[1] == "print_all":
	if len(sys.argv) != 2:
		print "error: print_all usage: no args..."
	else:
		print_all()
