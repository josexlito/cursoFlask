from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

'''
En las plantillas, se pueden utilizar estos bloques
    html:          Contiene el contenido completo de la etiqueta <html>.
    html_attribs:  Atribulos para la etiqueta <html>.
    head:          Contiene el contenido completo de la etiqueta <head>.
    body:          Contiene el contenido completo de la etiqueta <body>.
    body_attribs:  Atribulos para la etiqueta <body>.
    title:         Contiene el contenido completo de la etiqueta <title>.
    styles:        Contiene todos los estilos CSS de la etiqueta <link>.
    metas:         Contiene los <meta> de la cabacera.
    navbar:        Un bloque vacío encima del contenido.
    content:       Bloque para poner nuestro contenido.
    scripts:       Contiene todos los scripts en la etiqueta <script> al final del body.
'''

@app.route('/hola/')
@app.route('/hola/<nombre>')
def saluda(nombre=None):
    return render_template("template2.html", nombre=nombre)