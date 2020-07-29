from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

@app.route('/calculadora_post', methods=["get", "post"])
def calculadora_post():
    if request.method=='POST':
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operador = request.form.get("operador")

        try:
            resultado = eval(num1+operador+num2)
        except:
            return render_template("error.html", error="No se puede realizar la operación")

        return render_template("resultado.html", num1=num1, num2=num2, operador=operador, resultado=resultado)
    else:
        return render_template("calculadora_post.html")

@app.route("/calculadora_get", methods=["get"])
def calculadora_get():
	if request.method=="GET" and len(request.args)>0:
		num1=request.args.get("num1")
		num2=request.args.get("num2")
		operador=request.args.get("operador")
	
		try:
			resultado=eval(num1+operador+num2)
		except:
			return render_template("error.html",error="No puedo realizar la operación")
		
		return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	
	else:
		return render_template("calculadora_get.html")

@app.route("/calculadora/<operador>/<num1>/<num2>", methods=["get"])
def calculadora_var(operador,num1,num2):
	try:
		resultado=eval(num1+operador+num2)
	except:
			return render_template("error.html",error="No puedo realizar la operación")
	return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404	