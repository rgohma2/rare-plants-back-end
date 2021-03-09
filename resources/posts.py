import models
from models import DATABASE
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

posts = Blueprint('posts', 'posts')

@posts.route('/', methods=['GET'])
def get_all_posts():
	posts = models.Post.select()

	post_dicts = [model_to_dict(post) for post in posts]
	[post['user'].pop('password') for post in post_dicts]
	total_posts = len(post_dicts)

	return jsonify(
			data=post_dicts,
			total=total_posts,
			message=f'Sucessfully retrieved {len(posts)} posts',
			status=200
		), 200


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
			category=payload['category'],
			description=payload['description'] 
		)

	post_dict = model_to_dict(post)
	post_dict['user'].pop('password')

	return jsonify(
			data=post_dict,
			message='New post created!',
			status=200
		), 200

@posts.route('/<user_id>', methods=['GET'])
@login_required
def get_current_user_posts(user_id):
	posts = (models.Post
			.select()
			.where(models.Post.user == user_id))

	post_dicts = [model_to_dict(post) for post in posts]
	print(post_dicts)

	return jsonify(
			data=post_dicts,
			message=f'Sucessfully retrieved {len(posts)} posts.',
			status=200
		), 200






