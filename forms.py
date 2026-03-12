from wtforms import Form
from wtforms import StringField, IntegerField, EmailField,PasswordField
from wtforms import validators


class UserForm(Form):
    id=IntegerField("id")
    nombre=StringField('Nombre')
    apaterno=StringField('Apaterno')
    amaterno=StringField('Amaterno')
    edad=IntegerField("Edad")
    correo=EmailField('Correo')