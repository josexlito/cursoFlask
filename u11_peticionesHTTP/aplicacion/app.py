from flask import Flask, request
app = Flask(__name__)	

@app.route('/info', methods=['GET','POST'])
def inicio():
    cad = ""
    cad += "URL:" + request.url + "<br>"          # URL completa
    cad += "PATH:" + request.path + "<br>"        # ruta
    cad += "MÉTODO:" + request.method + "<br>"    # Método utilizado

    cad += "<h2>Header:</h2>"
    for item, value in request.headers.items():     # Cabeceras HTTP
        cad += "{}: {}<br>".format(item, value)
    
    cad += "<h2>Información en formularios (POST):</h2>"
    for item, value in request.form.items():        # Parámetros recibidos de un formulario por POST
        cad += "{}: {}<br>".format(item, value)
    
    cad += "<h2>Información en URL (GET):</h2>"     
    for item, value in request.args.items():        # Argumentos pasados por la URL por GET
        cad += "{}: {}<br>".format(item, value)
    
    cad += "<h2>Ficheros:</h2>"
    for item, value in request.files.items():       # Ficheros subidos al servidor
        cad += "{}: {}<br>".format(item, value)

    return cad

@app.route('/suma', methods=['GET', 'POST'])
def suma():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        return str(int(num1) + int(num2))
    else:
        salida = ''
        salida += '<form action="/suma" method="POST">'
        salida += '<label for="num1">Numero 1</label>'
        salida += '<input type="text" name="num1">'
        salida += '<label for="num2">Numero 2</label>'
        salida += '<input type="text" name="num2">'
        salida += '<input type="submit" value="Sumar">'
        salida += '</form>'
        return salida