from flask import Flask, render_template, abort
app = Flask(__name__)

@app.route('/hola/')
@app.route('/hola/<nombre>')
def saluda(nombre=None):
    return render_template("template1.html", nombre=nombre)

@app.route('/suma/<num1>/<num2>')
def suma(num1, num2):
    try:
        resultado=int(num1)+int(num2)
    except:
        abort(404)
    return render_template("template2.html", num1=num1, num2=num2, resultado=resultado)

@app.route('/multiplicar/<num>')
def multiplica(num):
    try:
        num=int(num)
    except:
        abort(404)
    return render_template("template3.html", num=num)

@app.route('/enlaces/')
def enlaces():
    links = [
        {"url":"www.google.es", "nombre":"Google"},
        {"url":"www.facebook.com", "nombre":"Facebook"},
        {"url":"www.twitter.com", "nombre":"Twitter"},
    ]
    return render_template("template4.html", links=links)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error404.html", error="Página no encontrada..."), 404