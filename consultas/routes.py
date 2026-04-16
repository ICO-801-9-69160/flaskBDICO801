from flask import Blueprint, render_template, request
from models import db, Alumnos, Curso, Inscripciones

consultas_bp = Blueprint('consultas_bp', __name__)

@consultas_bp.route("/consultas")
def menu_consultas():
    return render_template("consultas/menu_consultas.html")

@consultas_bp.route("/alumnos_curso", methods=["GET", "POST"])
def consulta_alumnos_curso():
    cursos = Curso.query.all()
    alumnos_inscritos = []
    curso_sel = None
    
    if request.method == "POST":
        curso_id = request.form.get("curso_id")
        curso_sel = Curso.query.get(curso_id)
        alumnos_inscritos = Inscripciones.query.filter_by(curso_id=curso_id).all()
        
    return render_template("consultas/alumnos_curso.html", 
                           cursos=cursos, 
                           inscripciones=alumnos_inscritos, 
                           curso_sel=curso_sel)

@consultas_bp.route("/cursos_alumno", methods=["GET", "POST"])
def consulta_cursos_alumno():
    alumnos = Alumnos.query.all()
    cursos_del_alumno = []
    alumno_sel = None
    
    if request.method == "POST":
        alumno_id = request.form.get("alumno_id")
        alumno_sel = Alumnos.query.get(alumno_id)
        cursos_del_alumno = Inscripciones.query.filter_by(alumno_id=alumno_id).all()
        
    return render_template("consultas/cursos_alumno.html", 
                           alumnos=alumnos, 
                           inscripciones=cursos_del_alumno, 
                           alumno_sel=alumno_sel)