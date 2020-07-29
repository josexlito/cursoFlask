from flask import Flask, make_response, abort, redirect, url_for
app = Flask(__name__)	

@app.route('/string/')                                              
def return_string():                                                # Con cabeceras estandar
    return "Hola mundo!"                                            # Texto estandar

@app.route('/object/')
def return_object():                                                
    headers = { 'Content-Type': 'text/plain'}                       # Cabeceras
    return make_response('Hola mundo!', 200, headers)               # Cuerpo, codigo de pagina, cabeceras

@app.route('/tuple/')
def return_tupla():                                                 # Similar que con make_response
    return "Hola mundo!", 200, {'Content-Type': 'text/plain'}       # Cuerpo, codigo de pagina y cabeceras

@app.route('/login')
def login():
    abort(401) # Se puede abortar la conexión, enviando reenviando a la pagina de error adecuada

@app.errorhandler(404)                              # El decorador errorhandler nos permite manejar mensajes de servidor como errores
def page_not_found(error):
    return "Pagina no encontrada:"+str(error), 404  # Mensaje de error

@app.route('/')
def index():                                    # redirect crea una redirección
    return redirect(url_for('return_string'))   # url_for construye la ruta de la función pasada por parámetros