from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")  #decorador
def inicio():
    return render_template("index.html")
     

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<int:contactoId>")
def editarContacto(contactoId):
    return render_template("editarContacto.html", id = contactoId)



    # /edad/20 naciste en el año 2000phiyon

app.run(debug=True)