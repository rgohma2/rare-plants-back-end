import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user


users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def test():
	return 'users resource working!'

@users.route('/register', methods=['POST'])
def register():
	"""User register route"""
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['user_name'] = payload['user_name'].lower()

	try:

		# check to see if there is user with same email registered
		if models.User.get(models.User.email == payload['email']):

			return jsonify(
				data={},
				message='There is already a user registered with that email.',
				status=401
			), 401

		# check to see if there is user with same username registered
		elif models.User.get(models.User.user_name == payload['user_name']):

			return jsonify(
				data={},
				message='There is already a user registered with that username.',
				status=401
			), 401

	except models.DoesNotExist:

		#encrypting password before creating it
		print(payload['password'])
		payload['password'] = generate_password_hash(payload['password'])
		print(payload['password'])

		return 'it worked'









