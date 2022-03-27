from flask import Blueprint, render_template, redirect, url_for
from modelsmessage import messages
from formsmessagesForm import ContactForm
from db import db


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        nombre = form.Nombre.data
        apellido = form.Apellido.data
        correo = form.Correo.data
        mensaje = form.Mensaje.data
        InsMssg = messages(nombre, apellido, correo, mensaje)
        db.session.add(InsMssg)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("main/main.html", form=form)


@main.route("/messages")
def message():
    List = messages.query.all()
    return render_template("main/messages.html", messagesList=List)

