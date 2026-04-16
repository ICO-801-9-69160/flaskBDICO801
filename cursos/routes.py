# cursos/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Curso, Maestros
import forms

cursos_bp = Blueprint('cursos_bp', __name__)

@cursos_bp.route("/cursos")
def cursos():
    cursos_list = Curso.query.all()
    return render_template("cursos/cursos.html", cursos=cursos_list)

@cursos_bp.route("/insertar_curso", methods=["GET", "POST"])
def insertar_curso():
    form = forms.CursoForm(request.form)

    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
    
    if request.method == 'POST' and form.validate():
        nuevo = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('cursos_bp.cursos'))
        
    return render_template('cursos/insertar_curso.html', form=form)

@cursos_bp.route("/modificar_curso", methods=["GET", "POST"])
def modificar_curso():
    curso_id = request.args.get('id')
    curso = Curso.query.get(curso_id)
    
    form = forms.CursoForm(request.form, obj=curso)

    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
    
    if request.method == 'POST' and form.validate():
        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data
        db.session.commit()
        return redirect(url_for('cursos_bp.cursos'))
        
    if request.method == 'GET':
        form.maestro_id.data = curso.maestro_id
        
    return render_template('cursos/modificar_curso.html', form=form, curso=curso)

@cursos_bp.route("/eliminar_curso", methods=["GET", "POST"])
def eliminar_curso():
    curso_id = request.args.get('id')
    curso = Curso.query.get(curso_id)
    
    form = forms.CursoForm(obj=curso)
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
    
    if request.method == 'POST':
        if curso:
            db.session.delete(curso)
            db.session.commit()
        return redirect(url_for('cursos_bp.cursos'))
    
    if request.method == 'GET':
        form.maestro_id.data = curso.maestro_id
        
    return render_template('cursos/eliminar_curso.html', form=form, curso=curso)

@cursos_bp.route("/detalles_curso")
def detalles_curso():
    curso_id = request.args.get('id')
    curso = Curso.query.get(curso_id)
    return render_template('cursos/detalles_curso.html', curso=curso)