import models
from models import DATABASE

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user
from peewee import IntegrityError


users = Blueprint('users', 'users')


@users.route('/', methods=['GET'])
def test():
	return 'users resource working!'

@users.route('/register', methods=['POST'])
def register():
	"""User register route"""
	payload = request.get_json()
	print(payload)
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()

	try:

		# encrypting password before creating it
		payload['password'] = generate_password_hash(payload['password'])

		with DATABASE.atomic():

		# creating new user
			new_user = models.User.create(
					username=payload['username'],
					email=payload['email'],
					password=payload['password']
				)
		login_user(new_user)
		new_user_dict = model_to_dict(new_user)
		new_user_dict.pop('password')

		return jsonify (
				data=new_user_dict,
				message='Sucessfully created new user with username: {}'.format(new_user_dict['username']),
				status=200
			), 200


	except IntegrityError as e:

		print('ERROR ARGUMENTS')
		print(e.args[0])

		# using the peewee.integrity error to check if the email/username is taken

		if e.args[0] == 'UNIQUE constraint failed: user.email':
			
			return jsonify(
				data={},
				message='There is already a user registered with that email.',
				status=401
			), 401

		elif e.args[0] == 'UNIQUE constraint failed: user.username':

			return jsonify(
				data={},
				message='There is already a user registered with that username.',
				status=401
			), 401
		else:
			print('ERROR')
			return e


@users.route('/login', methods=['POST'])
def login():
	"""User login route"""
	payload = request.get_json()
	payload['login'].lower()

	login = payload['login']

	email_login = False

	if '@' in payload['login']:
		email_login = True

	try:
		user = None

		if email_login:
			user = models.User.get(models.User.email == payload['login'])
		else:
			user = models.User.get(models.User.username == payload['login'])
		user_dict = model_to_dict(user)
		password_matches = check_password_hash(user_dict['password'], payload['password'])
		if password_matches:
			login_user(user)
			user_dict.pop('password')
			return jsonify(
					data=user_dict,
					message=f'Welcome back {login}',
					status=201
				), 201
		else:
			print('bad password')
			return jsonify(
					data={},
					message='Incorrect login or password.',
					status=401
				), 401			

	except models.DoesNotExist:
		print('bad login')
		return jsonify(
				data={},
				message='Incorrect login or password.',
				status=401
			), 401


@users.route('/logout', methods=['GET'])
def logout():
	print(current_user)
	logout_user()
	print(current_user)
	print('logged out')
	return jsonify(
			data={},
			message='Sucessfully logged out user.',
			status=200
		), 200









		








