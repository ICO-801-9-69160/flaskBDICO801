from wtforms import Form
from wtforms import StringField, IntegerField, EmailField, PasswordField
from wtforms import validators

class UserForm(Form):
    nombre = StringField("Nombre")
    apaterno = StringField("Apellido Paterno")
    amaterno = StringField("Apellido Mateno")
    edad = IntegerField("Edad")
    correo = EmailField("Correo Electronico")


