from flask import Flask, render_template, abort
app = Flask(__name__)

@app.route('/hola/')
@app.route('/hola/<nombre>')
def saluda(nombre=None):
    return render_template("template1.html", nombre=nombre)