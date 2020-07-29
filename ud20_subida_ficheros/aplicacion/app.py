from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from os import listdir
from aplicacion.forms import UploadForm
from werkzeug.utils import secure_filename

# form.data -> Diccionario con los llaves y valores del formulario
# form.errors -> Diccionario con los errores recibidos en el formulario
# form.validate_on_submit() -> Devuelve TRUE si ha sido validado correctamente
# form.num1 -> Campo
# form.num1.data -> Valor del campo
# form.num1() -> Devuelve la generación del campo en HTML
# form.num1.label -> Devuelve la generación de la etiqueta en HTML

app = Flask(__name__)
# Para obtener una secret_key, consultar aqui: https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502
# import secrets \n secrets.token_urlsafe(16)
app.secret_key = '4708tROORiMwgGyI-obgbw'
Bootstrap(app)

@app.route('/')
def inicio():

	lista = []
	for file in listdir(app.root_path+"/static/img"):
		lista.append(file)

	return render_template('inicio.html', lista=lista)

@app.route('/upload', methods=['get', 'post'])
def upload():
	form= UploadForm() # carga request.from y request.file
	if form.validate_on_submit():
		f = form.photo.data
		filename = secure_filename(f.filename)
		f.save(app.root_path+"/static/img/"+filename)
		return redirect(url_for('inicio'))
	return render_template('upload.html', form=form)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404	