import models
from models import DATABASE

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user
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

		if e.args[0] == 'UNIQUE constraint failed: user.email':
			return 'bad email'
		else:
			return 'bad username'


		








