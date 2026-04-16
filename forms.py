from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, IntegerField, EmailField, SelectField
from wtforms import validators



class UserForm(Form):
    id=IntegerField("ID")
    nombre=StringField('Nombre')
    apaterno=StringField('Apaterno')
    amaterno=StringField('Amaterno')
    edad=IntegerField("Edad")
    correo=EmailField('Correo')

class MaestrosForm(Form):
    matricula=IntegerField('matricula', [
        validators.DataRequired(message="El campo es requerido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=30, message="Ingrese un nombre válido")
    ])
    apellidos=StringField('Apellidos', [
        validators.DataRequired(message="El campo es requerido")
    ])
    especialidad=StringField('Especialidad', [
        validators.DataRequired(message="Ingrese una especialidad válida")
    ])
    email=EmailField('Email', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo válido")
    ])

class CursoForm(FlaskForm):
    id = IntegerField('ID')
    nombre = StringField('Nombre del Curso')
    descripcion = StringField('Descripción')
    maestro_id = SelectField('Asignar Maestro', coerce=int) 


class InscripcionForm(FlaskForm):
    alumno_id = SelectField('Seleccionar Alumno', coerce=int, validators=[validators.DataRequired()])
    curso_id = SelectField('Seleccionar Curso', coerce=int, validators=[validators.DataRequired()])