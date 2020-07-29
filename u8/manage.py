from flask_script import Manager
from aplicacion.app import app

# Manejador
# Éste gestiona el servidor web de Desarrollo y maneja las rutas de la aplicación
# runserver -> inicia el servidor
# Ejemplo: python3 manage.py runserver -h 0.0.0.0 -p 8080

manager = Manager(app)
app.config['DEBUG'] = True

if __name__ == '__main__':
    manager.run()