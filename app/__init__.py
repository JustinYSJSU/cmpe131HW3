from flask import Flask


myApp = Flask(__name__)
myApp.config.from_mapping(SECRET_KEY = 'you-will-never-guess')

from app import routes
