from jinja2 import Template

# Formas de presentar las plantillas (con render)
temp1 = 'Hola {{nombre}}'
print(Template(temp1).render(nombre='Pepe'))

# Varias variables
temp2 = '<a href="{{ url }}"> {{ enlace }}</a>'
print(Template(temp2).render(url='http://www.google.es', enlace='Ir a Google'))

# Tuplas
temp3 = '<a href="{{ datos[0] }}"> {{ datos[1] }}</a>'
print(Template(temp3).render(datos=['http://www.google.es', 'Ir a Google']))

# Diccionario
temp4 = '<a href="{{ datos.url }}"> {{ datos.enlace }}</a>'
print(Template(temp4).render(datos={'url':'http://www.google.es', 'enlace':'Ir a Google'}))

# Se pueden mandar datos a plantillas y modificar los datos (filtros) mediante métodos de cadena
# Primero la variable y seguido de barras y funciones
temp5 = 'Hola {{ nombre | striptags | title }}'
print(Template(temp5).render(nombre="     pepe  "))
temp6 = 'Colores: {{ lista | join(", ") }}'
print(Template(temp5).render(lista=['azul', 'amarillo', 'morado']))

