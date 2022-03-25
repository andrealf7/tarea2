from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from routes.messages import message
from routes.mainsite import main

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

# register blueprints
app.register_blueprint()
app.register_blueprint()
