from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Alumnos
import forms

alumnos_bp = Blueprint('alumnos_bp', __name__)

@alumnos_bp.route("/alumnos", methods=["GET"])
def alumnos():
    alumnos_list = Alumnos.query.all()
    return render_template("alumnos/alumnos.html", alumnos=alumnos_list)

@alumnos_bp.route("/insertar_alumno", methods=['GET', 'POST'])
def insertar_alumno():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            amaterno=create_form.amaterno.data,
            edad=create_form.edad.data,
            correo=create_form.correo.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos_bp.alumnos'))
    return render_template("alumnos/insertar_alumno.html", form=create_form)

@alumnos_bp.route("/modificar_alumno", methods=['GET', 'POST'])
def modificar_alumno():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
         id = request.args.get('id')
         alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
         create_form.id.data = request.args.get('id')
         create_form.nombre.data = alum1.nombre
         create_form.apaterno.data = alum1.apaterno
         create_form.amaterno.data = alum1.amaterno
         create_form.edad.data = alum1.edad
         create_form.correo.data = alum1.correo
    
    if request.method == 'POST':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nombre = create_form.nombre.data
        alum1.apaterno = create_form.apaterno.data
        alum1.amaterno = create_form.amaterno.data
        alum1.edad = create_form.edad.data
        alum1.correo = create_form.correo.data
        db.session.commit()
        return redirect(url_for('alumnos_bp.alumnos'))
    return render_template("alumnos/modificar.html", form=create_form)

@alumnos_bp.route('/eliminar_alumno', methods=['GET', 'POST'])
def eliminar_alumno():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
         id = request.args.get('id')
         alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
         create_form.id.data = request.args.get('id')
         create_form.nombre.data = alum1.nombre
         create_form.apaterno.data = alum1.apaterno
         create_form.amaterno.data = alum1.amaterno
         create_form.edad.data = alum1.edad    
         create_form.correo.data = alum1.correo
    if request.method == 'POST':
         id = request.form.get('id')
         alum = Alumnos.query.get_or_404(id)
         db.session.delete(alum) 
         db.session.commit()
         return redirect(url_for('alumnos_bp.alumnos'))
    return render_template('alumnos/eliminar.html', form=create_form)

@alumnos_bp.route("/detalles_alumno", methods=['GET'])
def detalles_alumno():
    id = request.args.get('id')
    alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
    return render_template('alumnos/detalles.html', id=id, nombre=alum1.nombre, apaterno=alum1.apaterno, amaterno=alum1.amaterno, edad=alum1.edad, correo=alum1.correo)