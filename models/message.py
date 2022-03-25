from email import message
from utils.db import db 

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    message = db.Column(db.String(600), nullable=False)

    def __init__(self, name, lastname, email, message) -> None:
        self.name = name
        self.lastname = lastname
        self.email = email
        self.message = message

    def __repr__(self) -> str:
        return f"Messaje({self.id}, '{self.name}', '{self.lastname}', '{self.email}', '{self.message})"
