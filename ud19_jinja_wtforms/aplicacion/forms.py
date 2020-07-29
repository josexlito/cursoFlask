from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import Required

class formCalculadora(FlaskForm):
    num1 = IntegerField("Número 1", validators=[Required("Introduzca un dato")])
    num2 = IntegerField("Número 2", validators=[Required("Introduzca un dato")])
    operador = SelectField("Operador", choices=[
        ("+", "Sumar"),
        ("-", "Restar"),
        ("*", "Multiplicar"),
        ("/", "Dividir"),
    ])

    submit = SubmitField('Submit')