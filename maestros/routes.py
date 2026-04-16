from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Maestros, Curso
import forms

maestros_bp = Blueprint('maestros_bp', __name__)

@maestros_bp.route("/maestros", methods=["GET"])
def maestros():
    maestros_list = Maestros.query.all()
    return render_template("maestros/maestros.html", maestros=maestros_list)

@maestros_bp.route("/insertar_maestro", methods=["GET", "POST"])
def insertar_maestro():
    form = forms.MaestrosForm(request.form)
    error = None
    
    if request.method == 'POST' and form.validate():
        maestro_existente = Maestros.query.filter_by(matricula=form.matricula.data).first()
        if maestro_existente:
            error = "Esa matrícula ya está registrada."
        else:
            nuevo_maestro = Maestros(
                matricula=form.matricula.data,
                nombre=form.nombre.data,
                apellidos=form.apellidos.data,
                especialidad=form.especialidad.data,
                email=form.email.data
            )
            db.session.add(nuevo_maestro)
            db.session.commit()
            return redirect(url_for('maestros_bp.maestros'))
            
    return render_template('maestros/insertar_maestro.html', form=form, error=error)

@maestros_bp.route("/modificar_maestro", methods=["GET", "POST"])
def modificar_maestro():
    form = forms.MaestrosForm(request.form)
    
    if request.method == 'GET':
        mat = request.args.get('mat')
        maestro = Maestros.query.filter_by(matricula=mat).first()
        form.matricula.data = maestro.matricula
        form.nombre.data = maestro.nombre
        form.apellidos.data = maestro.apellidos
        form.especialidad.data = maestro.especialidad
        form.email.data = maestro.email
        
    if request.method == 'POST':
        mat = form.matricula.data
        maestro = Maestros.query.filter_by(matricula=mat).first()
        maestro.nombre = form.nombre.data
        maestro.apellidos = form.apellidos.data
        maestro.especialidad = form.especialidad.data
        maestro.email = form.email.data
        
        db.session.commit()
        return redirect(url_for('maestros_bp.maestros'))
        
    return render_template('maestros/modificar_maestro.html', form=form)

@maestros_bp.route("/eliminar_maestro", methods=["GET", "POST"])
def eliminar_maestro():
    mat = request.args.get('mat')
    maestro = Maestros.query.get(mat)
    form = forms.MaestrosForm(obj=maestro)
    
    if request.method == 'POST':
        if maestro:
            cursos_vinculados = Curso.query.filter_by(maestro_id=mat).all()
            for c in cursos_vinculados:
                c.maestro_id = None
            
            db.session.flush() 
            
            db.session.delete(maestro)
            db.session.commit()
            
        return redirect(url_for('maestros_bp.maestros'))
        
    return render_template('maestros/eliminar_maestro.html', form=form, maestro=maestro)

@maestros_bp.route("/detalles_maestro", methods=["GET"])
def detalles_maestro():
    mat = request.args.get('mat')
    maestro = Maestros.query.filter_by(matricula=mat).first()
    return render_template('maestros/detalles_maestro.html', maestro=maestro)