print ('Hell0 W0rld')
from flask import Flask, jsonify


DEBUG = True
PORT = 8000

app = Flask(__name__)






















if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)