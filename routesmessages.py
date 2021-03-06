from flask import Blueprint, render_template
from db import db
from modelsmessage import Message
from sqlalchemy import desc

messages = Blueprint("messages", __name__, url_prefix="/messages")

@messages.route("/")
def home():
    messagesdf = Message.query.all().order_by(desc(Message.id))
    return render_template("messages.html", received = messagesdf)
