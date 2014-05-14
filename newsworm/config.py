from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

DEBUG = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
