import sys
import peewee
from models import *
from actions import *

action_list = ["create", "print", "insert", "delete", "print_batch_by_school", "print_student_by_batch", "print_student_by_school", "print_family", "age_average", "change_batch", "print_all", "note_average_by_student", "note_average_by_batch", "note_average_by_school", "top_batch", "top_school"]
table_list = ["school", "batch", "student", "exercise"]
models = {
	'school': School,
	'batch': Batch,
	'user': User,
	'student': Student,
	'exercise': Exercise
}

#
def top_school(*args, **kwargs):
	def top_school_subject(subject, school_id):
		best = None
		best_score = -1
		batches = Batch.select().where(Batch.school == school_id)
		if not batches:
			print "No batches in school"
			return
		for batch in batches:
			students = Student.select().where(Student.batch == batch)
			for student in students:
				total = 0
				count = 0
				for ex in Exercise.select().where(Exercise.student == student, Exercise.subject == subject[1]):
					total += ex.note
					count += 1
				if count == 0:
					count += 1
				avg = total/float(count)
				if avg > best_score:
					best = student
					best_score = avg
		return (best_score, str(best))

	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `top_school`")
	school_id = sys.argv[2]
	if not School.select().where(School.id == school_id):
		print "School not found"
		return
	if len(sys.argv) > 3:
		subject = sys.argv[3]
		best = top_school_subject(subject, school_id)
		if best:
			print best[1]
	else:
		winners = []
		for subject in Exercise.SUBJECTS:
			best = top_school_subject(subject, school_id)
			if best:
				winners.append(best)
		best = max(winners, key=lambda x: x[0])
		if best:
			print best[1]

#
def top_batch(*args, **kwargs):
	def top_batch_subject(subject, batch_id):
		best = None
		best_score = -1
		students = Student.select().where(Student.batch == batch_id)
		if not students:
			print "No students in batch"
			return
		for student in students:
			total = 0
			count = 0
			for ex in Exercise.select().where(Exercise.student == student, Exercise.subject == subject[1]):
				total += ex.note
				count += 1
			if count == 0:
				count += 1
			avg = total/float(count)
			if avg > best_score:
				best = student
				best_score = avg
		return (best_score, str(best))

	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `top_batch`")
	batch_id = sys.argv[2]
	if not Batch.select().where(Batch.id == batch_id):
		print "Batch not found"
		return
	if len(sys.argv) > 3:
		subject = sys.argv[3]
		best = top_batch_subject(subject, batch_id)
		if best:
			print best[1]
	else:
		winners = []
		for subject in Exercise.SUBJECTS:
			best = top_batch_subject(subject, batch_id)
			if best:
				winners.append(best)
		best = max(winners, key=lambda x: x[0])
		if best:
			print best[1]

#
def note_average_by_school():
	school_id = sys.argv[2]
	if not School.select().where(School.id == school_id):
		print "School not found"
		return
	for subject in Exercise.SUBJECTS:
		total = 0
		count = 0
		for batch in Batch.select().where(Batch.school == school_id):
			for student in Student.select().where(Student.batch == batch):
				for ex in Exercise.select().where(Exercise.student == student, Exercise.subject == subject[1]):
					total += ex.note
					count += 1
		if count == 0:
			continue;
		print str(subject[1]) + ": " + str(total/float(count))

#
def note_average_by_batch():
	try:
		batch_id = sys.argv[2]
		for subject in Exercise.SUBJECTS:
			note_sum = 0
			nb_notes = 0
			for student in Student.select().where(Student.batch==batch_id):
				for exercise in Exercise.select().where(Exercise.student==student, Exercise.subject==subject[1]):
					note_sum += exercise.note
					nb_notes += 1
			if nb_notes == 0:
				continue;
			print str(subject[1]) + ": " + str(note_sum/float(nb_notes))
	except:
		print "Batch not found"

#
def note_average_by_student():
	try:
		stu_id = sys.argv[2]
		for subject in Exercise.SUBJECTS:
			note_sum = 0
			nb_notes = 0
			for exercise in Exercise.select().where(Exercise.student==stu_id, Exercise.subject==subject[1]):
				note_sum += exercise.note
				nb_notes += 1
			if nb_notes == 0:
				continue;
			print str(subject[1]) + ": " + str(note_sum/nb_notes)
	except:
		print "Student not found"
#
def print_all():
	for school in School.select():
		print school
		for batch in school.batches:
			print "\t", batch
			for student in batch.students:
				print "\t\t", student
				for exercise in student.exercises:
					print "\t\t\t", exercise

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
	elif sys.argv[2] == "exercise":
		obj = Exercise.create(
			student=sys.argv[3],
			subject=sys.argv[4],
			note=sys.argv[5]
		)
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
	my_models_db.create_tables([BaseModel, School, Batch, User, Student, Exercise])
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
		elif sys.argv[2] == "exercise":
			print_table(Exercise)
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
#
elif sys.argv[1] == "note_average_by_student":
	if len(sys.argv) != 3:
		print "error: note_average_by_student usage: <student id>"
	else:
		note_average_by_student()
#
elif sys.argv[1] == "note_average_by_batch":
	if len(sys.argv) != 3:
		print "error: note_average_by_batch usage: <batch id>"
	else:
		note_average_by_batch()
#
elif sys.argv[1] == "note_average_by_school":
	if len(sys.argv) != 3:
		print "error: note_average_by_school usage: <school id>"
	else:
		note_average_by_school()
#
elif sys.argv[1] == "top_batch":
	if len(sys.argv) < 3:
		print "error: action_top_batch usage: <batch id> (<subject>)"
	else:
		top_batch()
#
elif sys.argv[1] == "top_school":
	if len(sys.argv) < 3:
		print "error: action_top_school usage: <school id> (<subject>)"
	else:
		top_school()
