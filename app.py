print ('Hell0 W0rld')
from flask import Flask, jsonify

import models

from resources.users import users
DEBUG = True
PORT = 8000



app = Flask(__name__)
app.secret_key = "big ol' secret"


app.register_blueprint(users, url_prefix='/api/v1/users')










if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)