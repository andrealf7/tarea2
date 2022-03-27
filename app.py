from flask import Flask
from routesmainsite import main


app = Flask(__name__)
app.config.from_object("config.BaseConfig")


# register blueprints
app.register_blueprint(main)

