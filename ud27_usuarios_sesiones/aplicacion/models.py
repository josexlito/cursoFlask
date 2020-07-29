from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Categorias(db.Model):
	"""Categorías de los artículos"""
    # Nombre de la tabla
	__tablename__ = 'categorias'
    # Atributos -> Columnas de la bbdd
	id = Column(Integer, primary_key=True)
	nombre = Column(String(100))
    # Relaciones
	articulos = relationship("Articulos", cascade="all, delete-orphan", backref="Categorias",lazy='dynamic')

    # Sobreescritura de métodos heredados
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Articulos(db.Model):
	"""Artículos de nuestra tienda"""
	__tablename__ = 'articulos'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(100),nullable=False)
	precio = Column(Float,default=0)
	iva = Column(Integer,default=21)
	descripcion = Column(String(255))
	image = Column(String(255))
	stock = Column(Integer,default=0)
	CategoriaId=Column(Integer,ForeignKey('categorias.id'), nullable=False)
	categoria = relationship("Categorias", backref="Articulos")

	def precio_final(self):
		return self.precio+(self.precio*self.iva/100)

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))


class Usuarios(db.Model):
    """Usuarios"""
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(100),nullable=False)
    password_hash = Column(String(128),nullable=False)
    nombre = Column(String(200),nullable=False)
    email = Column(String(200),nullable=False)
    admin = Column(Boolean, default=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))    

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')    

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

"""
 cat = Categorias(nombre="Arcade") -> Creamos un objeto de 'models' y le pasamos los campos con sus valores
 db.session.add(cat) -> El objeto se va a añadir a la BBDD
 db.session.commit() -> Lanzar la ejecución contra la BBDD

 art1 = Articulos(nombre="PAC MAN", precio=12, descripcion="Juego de fantasmitas", stock=1, CategoriaId=1) -> Indica manualmente la categoría
 art2 = Articulos(nombre="Super Mario Bros", precio=25, descripcion="Juego de plataformas", stock=10, categoria=cat) -> Se le pasa la categoría con la relación
 db.session.add_all([art1, art2]) -> Hacer varias adiciones con una lista

 Hacer update
 art1.precio = 15
 db.session.add(art1)
 db.session.commit()

 db.session.delete(art2) -> Eliminar registro

 Selects

 art = Articulos.query.first() -> el objeto 'art' será el primer registro de la tabla Articulos

 art = Articulos.query.get(2) -> el objeto 'art' será el registro numero 2 de la tabla
 
 articulos = Articulos.query.all() -> Lista con todos los articulos

 Articulos.query.count() -> Número de registros

 Articulos.query.filter_by(precio=25).all() -> Devuelve una lista filtrada por precio = 25 de todos los registros de Articulos

 Articulos.query.order_by("precio").all() -> Devuelve una lista ordenada en base al precio de todos los registros de Articulos

"""