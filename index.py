from flask_sqlalchemy import SQLAlchemy
from app import app

from db import db

SQLAlchemy(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)