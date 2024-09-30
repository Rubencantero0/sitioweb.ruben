from flask import Flask, render_template
from flask_bootstrap import bootstrap

app = Flask(__name__)
bootstrap(app)

@app.route("/")
def inicio ():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/servicios")
def nosotros():
    return render_template("servicios.html")

@app.route("/contacto")
def nosotros():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)

