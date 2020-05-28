from app import app
from app.api import API
from flask import request
from flask_cors import cross_origin

@app.route('/', methods=['GET'])
def index():
	return "Hello stranger..."