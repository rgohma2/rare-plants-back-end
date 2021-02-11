import models
from models import DATABASE
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

posts = Blueprint('posts', 'posts')

@posts.route('/', methods=['GET'])
def test():
	return 'posts resource working!'



