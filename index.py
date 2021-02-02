from flask import Flask, render_template, request, redirect

app=Flask(__name__)

tareas = []
tareas2 = ['casa','auto']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacto')
def contacto():
    return 'hola contacto'

@app.route('/ejemplo1')
def ejemplo1():
    nombre='Name'
    otropy='otro valor'
    return render_template('ejemplo1.html',nombre=nombre,otro=otropy,tareas2=tareas2)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/recibedeformulario', methods=["POST"])
def recibedeformulario():
    nombre=request.form.get("nombre")
    return render_template('recibedeformulario.html', nombre=nombre)

@app.route('/indexa')
def indexa():
    return render_template('indexa.html', tareas=tareas)

@app.route('/agregar', methods=["GET", "POST"])
def agregar():
    if request.method == "GET":
        return render_template('agregar.html')
    else:
        tarea = request.form.get("tarea")
        tareas.append(tarea)
        return redirect("/indexa")
    
if __name__ ==  '__main__':
    app.run(debug=True)
