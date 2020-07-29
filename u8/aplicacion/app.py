from flask import Flask
app = Flask(__name__)

# Aplicación

@app.route('/')
def hola_mundo():
    return 'Hola mundo'