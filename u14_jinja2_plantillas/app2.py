from jinja2 import Template

# bucle FOR

# En un bloque for tenemos acceso a varias variables, veamos las más interesantes:
# loop.index: La iteración actual del bucle (empieza a contar desde 1).
# loop.index0: La iteración actual del bucle (empieza a contar desde 0).
# loop.first: True si estamos en la primera iteración.
# loop.last: True si estamos en la última iteración.
# loop.length: Número de iteraciones del bucle.

# El `-` detrás del bloque for evita que se añada una línea en blanco.
temp8 = '''
<ul>
    {% for elem in elements -%}
        <li>{{loop.index}} - {{elem}}</li>
    {% endfor -%}
</ul>
'''

print(Template(temp8).render(elements=['azul', 'amarillo', 'morado']))

# bloque IF
temp9='''
{% if elems %}
<ul>
{% for elem in elems -%}
    {% if elem is divisibleby 2 -%}
        <li>{{elem}} es divisible por 2.</li>
    {% else -%}
        <li>{{elem}} no es divisible por 2.</li>
    {% endif -%}
{% endfor -%}
</ul>
{% endif %}
'''
print(Template(temp9).render(elems=[1,2,3,4]))