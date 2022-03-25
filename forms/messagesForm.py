from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, Email

class Messages(FlaskForm):
    name = StringField(
        validators=[
            InputRequired(),
            Length(min=2, max=20),
        ],
        render_kw={"placeholder": "Name"},
    )
    lastname = StringField(
        validators=[
            InputRequired(),
            Length(min=2, max=20),
        ],
        render_kw={"placeholder": "Lastname"},
    )
    email = StringField(
        validators=[
            InputRequired(),
            Length(min=5, max=60),
            Email(),
        ],
        render_kw={"placeholder": "E-mail"},
    )
    message = StringField(
        validators=[
            InputRequired(),
            Length(min=2, max=600),
        ],
        render_kw={"placeholder": "Message"},
    )
    
    submit = SubmitField("ENVIAR")
