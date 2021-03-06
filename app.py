print ('Hell0 W0rld')
from flask import Flask, jsonify
from flask_login import LoginManager
from flask_cors import CORS

import models

from resources.users import users
from resources.posts import posts


DEBUG = True
PORT = 8000



app = Flask(__name__)

CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(posts, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(users, url_prefix='/api/v1/users')

app.register_blueprint(posts, url_prefix='/api/v1/posts')

app.secret_key = "big ol' secret"

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
	try:
		return models.User.get(models.User.id == user_id)
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
			data={},
			message='Error, user not logged in',
			status=401
		), 401 












if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)