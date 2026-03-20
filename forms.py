from wtforms import Form
from wtforms import StringField, IntegerField, EmailField
from wtforms import validators
from wtforms import Form, StringField, IntegerField, SelectField, validators

class UserForm(Form):
    id = IntegerField("Matricula")
    nombre = StringField('Nombre')
    apaterno = StringField('Apaterno')
    amaterno = StringField('Amaterno')
    edad = IntegerField("Edad")
    correo = EmailField('Correo')

class MaestroForm(Form):
    matricula = IntegerField("Matricula")
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    especialidad = StringField('Especialidad')
    correo = EmailField('Correo')

class CursoForm(Form):
    nombre = StringField('Nombre del Curso', [validators.DataRequired()])
    descripcion = StringField('Descripción')
    maestro_id = SelectField('Maestro que imparte', coerce=int)


class InscripcionForm(Form):
    alumno_id = SelectField('Alumno', coerce=int)
    curso_id = SelectField('Curso', coerce=int)