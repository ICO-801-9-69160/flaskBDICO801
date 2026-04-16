from flask import Blueprint, flash, render_template, request, redirect, url_for
from models import db, Alumnos, Curso, Inscripciones
import forms

inscripciones_bp = Blueprint('inscripciones_bp', __name__)

@inscripciones_bp.route("/inscripciones", methods=["GET"])
def inscripciones():
    lista_inscripciones = Inscripciones.query.all()
    return render_template("inscripciones/inscripciones.html", inscripciones=lista_inscripciones)

@inscripciones_bp.route("/insertar_inscripcion", methods=["GET", "POST"])
def insertar_inscripcion():
    form = forms.InscripcionForm(request.form)
    
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno}") for a in Alumnos.query.all()]
    form.curso_id.choices = [(c.id, c.nombre) for c in Curso.query.all()]
    
    if request.method == 'POST' and form.validate():
        inscripcion_existente = Inscripciones.query.filter_by(
            alumno_id=form.alumno_id.data, 
            curso_id=form.curso_id.data
        ).first()
        
        if inscripcion_existente:
            flash("El alumno ya está inscrito en este cursoo.")
        else:
            nueva_inscripcion = Inscripciones(
                alumno_id=form.alumno_id.data,
                curso_id=form.curso_id.data
            )
            db.session.add(nueva_inscripcion)
            db.session.commit()
            return redirect(url_for('inscripciones_bp.inscripciones'))
            
    return render_template('inscripciones/insertar_inscripcion.html', form=form)

@inscripciones_bp.route("/modificar_inscripcion", methods=["GET", "POST"])
def modificar_inscripcion():
    ins_id = request.args.get('id')
    inscripcion = Inscripciones.query.get(ins_id)
    
    form = forms.InscripcionForm(request.form, obj=inscripcion)
    
    # Recargar opciones de los desplegables
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno}") for a in Alumnos.query.all()]
    form.curso_id.choices = [(c.id, c.nombre) for c in Curso.query.all()]
    
    if request.method == 'POST' and form.validate():
        inscripcion.alumno_id = form.alumno_id.data
        inscripcion.curso_id = form.curso_id.data
        db.session.commit()
        return redirect(url_for('inscripciones_bp.inscripciones'))
        
    if request.method == 'GET':
        form.alumno_id.data = inscripcion.alumno_id
        form.curso_id.data = inscripcion.curso_id
        
    return render_template('inscripciones/modificar_inscripcion.html', form=form, inscripcion=inscripcion)

@inscripciones_bp.route("/eliminar_inscripcion", methods=["GET", "POST"])
def eliminar_inscripcion():
    ins_id = request.args.get('id')
    inscripcion = Inscripciones.query.get(ins_id)
    
    form = forms.InscripcionForm(obj=inscripcion)
    
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno}") for a in Alumnos.query.all()]
    form.curso_id.choices = [(c.id, c.nombre) for c in Curso.query.all()]
    
    if request.method == 'POST':
        if inscripcion:
            db.session.delete(inscripcion)
            db.session.commit()
        return redirect(url_for('inscripciones_bp.inscripciones'))
        
    if request.method == 'GET':
        form.alumno_id.data = inscripcion.alumno_id
        form.curso_id.data = inscripcion.curso_id
        
    return render_template('inscripciones/eliminar_inscripcion.html', form=form, inscripcion=inscripcion)

@inscripciones_bp.route("/consulta_alumnos_curso", methods=["GET", "POST"])
def consulta_alumnos_curso():
    cursos = Curso.query.all()
    alumnos_inscritos = []
    curso_seleccionado = None
    
    if request.method == "POST":
        curso_id = request.form.get("curso_id")
        curso_seleccionado = Curso.query.get(curso_id)
        # Buscamos en Inscripciones filtrando por el curso
        alumnos_inscritos = Inscripciones.query.filter_by(curso_id=curso_id).all()
        
    return render_template("inscripciones/alumnos_curso.html", 
                           cursos=cursos, 
                           inscripciones=alumnos_inscritos, 
                           curso_sel=curso_seleccionado)

@inscripciones_bp.route("/consulta_cursos_alumno", methods=["GET", "POST"])
def consulta_cursos_alumno():
    alumnos = Alumnos.query.all()
    cursos_del_alumno = []
    alumno_seleccionado = None
    
    if request.method == "POST":
        alumno_id = request.form.get("alumno_id")
        alumno_seleccionado = Alumnos.query.get(alumno_id)

        cursos_del_alumno = Inscripciones.query.filter_by(alumno_id=alumno_id).all()
        
    return render_template("inscripciones/cursos_alumno.html", 
                           alumnos=alumnos, 
                           inscripciones=cursos_del_alumno, 
                           alumno_sel=alumno_seleccionado)