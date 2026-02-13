from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")

@app.route("/usuarios")
def usuarios():
	return render_template("usuario.html")

def index():
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
