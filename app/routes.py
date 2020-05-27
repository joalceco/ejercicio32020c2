from flask import render_template
from app import app
from app.forms import Ejercicio3Form

@app.route("/")
def index():
    return "Pagina de inicio"


def riman(palabra1, palabra2):
    if palabra1[-3:] == palabra2[-3:]:
        return "Si riman3"
    elif palabra1[-2:] == palabra2[-2:]:
        return "casi riman"
    return "no riman cuate"


# 3.- Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman.
#  Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
@app.route("/ejercicio3", methods=["GET", "POST"])
def ejercicio3():
    form = Ejercicio3Form()
    if form.validate_on_submit():
        #checar si riman
        msj = riman(form.palabra1.data,form.palabra2.data)
        return render_template("ejercicio3respuesta.html", msj=msj)
    return render_template("ejercicio3.html", form = form)

