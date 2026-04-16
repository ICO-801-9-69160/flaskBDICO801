from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from config import developmentConfig
from flask_migrate import Migrate
from models import db
from alumnos.routes import alumnos_bp
from maestros.routes import maestros_bp
from cursos.routes import cursos_bp
from inscripciones.routes import inscripciones_bp
from consultas.routes import consultas_bp

app = Flask(__name__)
app.config.from_object(developmentConfig)

db.init_app(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db)

app.register_blueprint(alumnos_bp)
app.register_blueprint(maestros_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(inscripciones_bp)
app.register_blueprint(consultas_bp)

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()