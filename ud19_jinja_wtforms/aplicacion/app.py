from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from aplicacion.forms import formCalculadora

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
    return render_template("inicio.html")

@app.route('/calculadora_post', methods=["get", "post"])
def calculadora_post():
	form = formCalculadora(request.form)
	if form.validate_on_submit():
		num1 = request.form.get('num1')
		num2 = request.form.get('num2')
		operador = request.form.get('operador')

		try:
			resultado = eval(num1+operador+num2)
		except:
			return render_template('error.html', error="No se puede llevar a cabo la operación")
		
		return render_template('resultado.html', num1=num1, num2=num2, operador=operador, resultado=resultado)
	else:
		return render_template('calculadora_post.html', form=form)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404	