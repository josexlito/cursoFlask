from flask import Flask
app = Flask(__name__)	

# Raíz
@app.route('/')
def inicio():
    return "Pagina de inicio";

# El nombre del recurso
@app.route('/acercade')
def acercade():
    return "Acerca de...";

# Si tiene una barra al final, si en el navegador no se indica, se produce redirección
@app.route('/articulos/')
def articulos():
    return "Lista de artículos";

# Si llegan parametros, se pueden obtener así
@app.route('/articulos/<int:id>')
def mostrar_articulo(id):
    return "Artículo con id: {}".format(id);

# Pueden llevar varias rutas distintas a la misma funcion
@app.route('/hola/')
@app.route('/hola/<string:nombre>')
@app.route('/hola/<string:nombre>/<int:edad>')
def hola(nombre=None, edad=None):
    if nombre and edad:
        return "Hola {0}, tienes {1} años.".format(nombre, edad)
    elif nombre:
        return "Hola {0}.".format(nombre)
    else:
        return "Hola, desconocido."