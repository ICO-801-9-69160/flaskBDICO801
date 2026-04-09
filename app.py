from flask import Flask, render_template, request, redirect, url_for
from flask import flash

from flask_wtf.csrf import CSRFProtect
from config import developmentConfig
from flask import g
from flask_migrate import Migrate
from models import db, Alumnos, Maestros

 
from models import db, Alumnos
import forms
app = Flask(__name__)
app.config.from_object(developmentConfig)


db.init_app(app)
csrf=CSRFProtect()
migrate=Migrate(app, db)



@app.route("/",methods=["GET","POST"])
@app.route("/index")
def index():
    create_alumno=forms.UserForm(request.form)
    #select * alumnos alumnos
    alumno=Alumnos.query.all()
    return render_template("index.html", form=create_alumno, alumno=alumno)

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apaterno=create_form.apaterno.data,
                     amaterno=create_form.amaterno.data,
                     edad=create_form.edad.data,
                     correo=create_form.correo.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("Alumnos.html",form=create_form)

@app.route("/modificar",methods=['GET','POST'])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
         id=request.args.get('id')
         #  select * from alumnos where id == id
         alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
         create_form.id.data=request.args.get('id')
         create_form.nombre.data=alum1.nombre
         create_form.apaterno.data=alum1.apaterno
         create_form.amaterno.data=alum1.amaterno
         create_form.edad.data=alum1.edad
         create_form.correo.data=alum1.correo
    
    if request.method=='POST':
        id=request.args.get('id')
         #  select * from alumnos where id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.id=id
        alum1.nombre=create_form.nombre.data
        alum1.apaterno=create_form.apaterno.data
        alum1.amaterno=create_form.amaterno.data
        alum1.edad=create_form.edad.data
        alum1.correo=create_form.correo.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("modificar.html",form=create_form)

@app.route('/eliminar',methods=['GET','POST'])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
         id=request.args.get('id')
         #  select * from alumnos where id == id
         alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
         create_form.id.data=request.args.get('id')
         create_form.nombre.data=alum1.nombre
         create_form.apaterno.data=alum1.apaterno
         create_form.amaterno.data=alum1.amaterno
         create_form.edad.data=alum1.edad    
         create_form.correo.data=alum1.correo
    if request.method=='POST':
         id=request.form.get('id')
         alum = Alumnos.query.get_or_404(id)
         #delete from alumnos where id=id
         db.session.delete(alum) 
         db.session.commit()
         return redirect(url_for('index'))
    return render_template('eliminar.html',form=create_form)

@app.route("/detalles",methods=['GET','POST'])
def detalles():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
         id=request.args.get('id')
         #  select * from alumnos where id == id
         alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
         id=request.args.get('id')
         nombre=alum1.nombre
         apaterno=alum1.apaterno
         amaterno=alum1.amaterno
         edad=alum1.edad     
         correo=alum1.correo
         
    return render_template('detalles.html',id=id,nombre=nombre,apaterno=apaterno,
                           amaterno=amaterno,edad=edad,correo=correo)






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
        mat=usuarios_clas.matricula.data
        nom=usuarios_clas.nombre.data
        apa=usuarios_clas.apaterno.data
        ama=usuarios_clas.amaterno.data
        edad=usuarios_clas.edad.data
        email=usuarios_clas.correo.data
    
    return render_template('usuarios.html',form=usuarios_clas,mat=mat,
                           nom=nom,apa=apa,ama=ama,edad=edad,email=email)


@app.route("/maestros", methods=["GET", "POST"])
def maestros():
    maestros_lista = Maestros.query.all()
    return render_template("maestros/maestros.html", maestros=maestros_lista)

@app.route("/insertar_maestro", methods=["GET", "POST"])
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
            return redirect(url_for('maestros'))
            
    return render_template('maestros/insertar_maestro.html', form=form, error=error)

@app.route("/modificar_maestro", methods=["GET", "POST"])
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
        return redirect(url_for('maestros'))
        
    return render_template('maestros/modificar_maestro.html', form=form)

@app.route("/eliminar_maestro", methods=["GET", "POST"])
def eliminar_maestro():
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
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for('maestros'))
        
    return render_template('maestros/eliminar_maestro.html', form=form)

@app.route("/detalles_maestro", methods=["GET"])
def detalles_maestro():
    mat = request.args.get('mat')
    maestro = Maestros.query.filter_by(matricula=mat).first()
    return render_template('maestros/detalles_maestro.html', maestro=maestro)

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()


