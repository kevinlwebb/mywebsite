from flask import Flask
from os import path

import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


from flaskapp import routes
