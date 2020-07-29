from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run('0.0.0.0', 8888, debug=True)