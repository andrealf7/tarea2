from db import db


class messages(db.Model):  


    idContacto = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)


    def __init__(
        self,
        firstname: str,
        lastname: str,
        email: str,
        message: str,
    ) -> None:

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.message = message

    def __repr__(self) -> str:
        return f"""Contactanos(
            {self.idContacto}, 
            {self.firstname}, 
            {self.lastname},
            {self.email},
            {self.message})"""
