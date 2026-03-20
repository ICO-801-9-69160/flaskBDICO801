from flask  import Flask, render_template,request, redirect, url_for
from flask import flash
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import developmentConfig
from models import db, Alumnos, Maestros, Curso, Inscripcion
import forms  

app = Flask(__name__)
app.config.from_object(developmentConfig)
db.init_app(app)
migrate=Migrate(app, db)
csrf = CSRFProtect(app)



@app.route("/")
def index():
    return render_template("bienvenida.html")

@app.route("/consulta/alumnos_por_curso/<int:id>")
def alumnos_por_curso(id):
    curso = Curso.query.get(id)
    return render_template("consulta_alumnos.html", curso=curso)

@app.route("/maestros",methods=["GET","POST"])
def maestros():
    mat=0
    nom=''
    ape=''
    esp=''
    email=''
    maestros_clas=forms.MaestroForm(request.form)
    if request.method=='POST':
        mat=maestros_clas.matricula.data
        nom=maestros_clas.nombre.data
        ape=maestros_clas.apellidos.data
        esp=maestros_clas.especialidad.data
        email=maestros_clas.correo.data
        
        # Guardar en la base de datos igual que Alumnos
        nuevo_maestro = Maestros(matricula=mat, nombre=nom, apellidos=ape, 
                                 especialidad=esp, email=email)
        db.session.add(nuevo_maestro)
        db.session.commit()
    
    # Select para mostrar en la tabla de maestros.html
    lista_maestros = Maestros.query.all()
    
    return render_template('maestros.html', form=maestros_clas, maestros=lista_maestros,
                           mat=mat, nom=nom, ape=ape, esp=esp, email=email)

@app.route("/usuarios", methods=["GET", "POST"])
def usuario():
    usuarios_clas = forms.UserForm(request.form)

    if request.method == 'POST' and usuarios_clas.validate():
        nuevo_alumno = Alumnos(
            id=usuarios_clas.id.data,
            nombre=usuarios_clas.nombre.data,
            apaterno=usuarios_clas.apaterno.data,
            correo=usuarios_clas.correo.data
        )
        db.session.add(nuevo_alumno)
        db.session.commit()
        flash("Alumno registrado con éxito")
        return redirect(url_for('usuario'))

    # CONSULTA DINÁMICA (CURSOS POR ALUMNO)
    ver_cursos_id = request.args.get("ver_cursos")

    cursos_alumno = []
    alumno_sel = None

    if ver_cursos_id:
        alumno_sel = Alumnos.query.get(ver_cursos_id)
        cursos_alumno = alumno_sel.cursos

    lista_alumnos = Alumnos.query.all()

    return render_template('usuarios.html',
                           form=usuarios_clas,
                           alumnos=lista_alumnos,
                           cursos_alumno=cursos_alumno,
                           alumno_sel=alumno_sel)

@app.route("/cursos", methods=["GET", "POST"])
def cursos():
    form = forms.CursoForm(request.form)

    # Select dinámico de maestros
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]

    if request.method == 'POST' and form.validate():
        nuevo_curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        return redirect(url_for('cursos'))

    # CONSULTA DINÁMICA (ALUMNOS POR CURSO)
    ver_alumnos_id = request.args.get("ver_alumnos")

    alumnos_curso = []
    curso_sel = None

    if ver_alumnos_id:
        curso_sel = Curso.query.get(ver_alumnos_id)
        alumnos_curso = curso_sel.alumnos

    lista_cursos = Curso.query.all()

    return render_template("cursos.html",
                           form=form,
                           cursos=lista_cursos,
                           alumnos_curso=alumnos_curso,
                           curso_sel=curso_sel)

@app.route("/inscripciones", methods=["GET", "POST"])
def inscripciones():
    form = forms.InscripcionForm(request.form)
    
    # Llenamos los selectores con Alumnos y Cursos reales
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno}") for a in Alumnos.query.all()]
    form.curso_id.choices = [(c.id, c.nombre) for c in Curso.query.all()]
    
    if request.method == 'POST':
        alumno = Alumnos.query.get(form.alumno_id.data)
        curso = Curso.query.get(form.curso_id.data)
        
        # Usamos append para crear la relación en la tabla 'inscripciones'
        curso.alumnos.append(alumno)
        db.session.commit()
        flash("Inscripción realizada con éxito")
        return redirect(url_for('inscripciones'))
        
    return render_template("inscripciones.html", form=form)

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()