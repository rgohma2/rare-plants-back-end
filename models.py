from peewee import *
import datetime

DATABASE = SqliteDatabase('plants.sqlite')

class BaseModel(Model):
	"""Our base model that all other models will inherit from"""
	class Meta:
		database = DATABASE


class User(BaseModel):
	user_name = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()
	date_created = DateTimeField(default=datetime.datetime.now)


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User], safe=True)
	print("successfully connected to database (:")
	DATABASE.close()
