import peewee as pw

my_models_db = pw.SqliteDatabase('my_models.db', pragmas = (('foreign_keys', True), ))

class BaseModel(pw.Model):
	"""docstring for BaseModel"""
	id = pw.PrimaryKeyField(unique=True)

	class Meta:
		database = my_models_db
		order_by = ('id', )

class School(BaseModel):
	"""docstring for School"""
	name = pw.CharField(128, null=False)

	def __str__(self):
		return "School: " + self.name + " (" + str(self.id) + ")"

class Batch(BaseModel):
	"""docstring for Batch"""
	school = pw.ForeignKeyField(School, related_name='batches', on_delete='CASCADE')
	name = pw.CharField(128, null=False)

	def __str__(self):
		return "Batch: " + self.name + " (" + str(self.id) + ")"

class User(BaseModel):
	"""docstring for User"""
	first_name = pw.CharField(128, default="")
	last_name = pw.CharField(128, null=False)
	age = pw.IntegerField(null=False)

	def __str__(self):
		return "User: " + self.first_name + " " + self.last_name + " (" + str(self.id) + ")"

class Student(User):
	"""docstring for Student"""
	batch = pw.ForeignKeyField(Batch, related_name='students', on_delete='CASCADE')

	def __str__(self):
		return "Student: " + self.first_name + " " + self.last_name + " (" + str(self.id) + ")" + " part of the batch: " + str(self.batch)
