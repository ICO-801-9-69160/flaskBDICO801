from flask  import Flask, render_template,request, redirect, url_for
from flask import flash
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import developmentConfig
from models import db, Alumnos
import forms


app = Flask(__name__)
app.config.from_object(developmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)


@app.route("/", methods=["GET","POST"])
@app.route("/index")
def index():
    create_alumno = forms.UserForm(request.form)
    #select * alumnos alumnossff 
    alumno = Alumnos.query.all()
    return render_template("index.html",form=create_alumno, alumno=alumno)


@app.route("/usuarios",methods=["GET","POST"])
def usuario():
    mat=0
    nom=''
    apa=''
    ama=''
    edad=0
    email=''
    usuarios_clas=forms.UserForm(request.form)
    if request.method=='POST':
        id=usuarios_clas.id.data
        nom=usuarios_clas.nombre.data
        apa=usuarios_clas.apaterno.data
        ama=usuarios_clas.amaterno.data
        edad=usuarios_clas.edad.data
        email=usuarios_clas.correo.data
    
    return render_template('usuarios.html',form=usuarios_clas,id=id,
                           nom=nom,apa=apa,ama=ama,edad=edad,email=email)

@app.route('/maestros', methods=['GET', 'POST'])
def maestros():
    mat = ''
    nomb = ''
    apell = ''
    esp = ''
    curs= ''
    maestros_class = forms.MaestroForm(request.form)
    if request.method == 'POST':
        mat=maestros_class.matricula.data
        nomb=maestros_class.nombre.data
        apell=maestros_class.apellidos.data
        esp=maestros_class.especialidad.data
        curs=maestros_class.curso.data
    return render_template('indexMaestros.html', form=maestros_class)

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()