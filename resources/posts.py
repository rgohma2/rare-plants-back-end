import models
from models import DATABASE
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

posts = Blueprint('posts', 'posts')

@posts.route('/', methods=['GET'])
def test():
	return 'posts resource working!'


@posts.route('/<user_id>', methods=['POST'])
@login_required
def make_post(user_id):
	payload = request.get_json()
	post = models.Post.create(
			user=user_id,
			title=payload['title'],
			price=payload['price'],
			seed_count=payload['seed_count'],
			image=payload['image'],
			category=payload['category'] 
		)

	post_dict = model_to_dict(post)
	post_dict['user'].pop('password')

	return jsonify(
			data=post_dict,
			message='New post created!',
			status=200
		), 200




