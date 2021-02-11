from peewee import *
import datetime

from flask_login import UserMixin

DATABASE = SqliteDatabase('plants.sqlite') 

class BaseModel(Model):
	"""Our base model that all other models will inherit from"""
	class Meta:
		database = DATABASE


class User(BaseModel, UserMixin):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()
	date_created = DateTimeField(default=datetime.datetime.now)

class Post(BaseModel):
	user = ForeignKeyField(User, backref='post')
	title = CharField()
	price = CharField()
	seed_count = CharField()
	image = CharField()
	category = CharField()
	date_created = DateTimeField(default=datetime.datetime.now)





def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Post], safe=True)
	print("successfully connected to database (:")
	DATABASE.close()
