from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PersonaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    apelido = StringField('Apellido')
    email = StringField('Email',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

