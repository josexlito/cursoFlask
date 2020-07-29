from flask import Flask, request
app = Flask(__name__)	

# Raíz
@app.route('/')
def inicio():
    return "Pagina de inicio";

@app.route('/articulos/')
def articulos():
    return "Lista de artículos";

# Se pueden definir los métodos admitidos
@app.route('/articulos/new', methods=['POST'])
def nuevo_articulo():
    return "Esta URL recibe la información de un formulario con el método POST";

# Pueden llevar varias rutas distintas a la misma funcion
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Accedido con POST"
    else:
        return "Accedido con GET"