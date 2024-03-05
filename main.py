from flask import Flask, render_template, request, redirect, url_for
from forms import UserForm
from flask import flash 
from flask import g
from flask_wtf.csrf import CSRFProtect
from config import DevConfig
app = Flask(__name__)
from models import db
from forms import UserForm
from models import Alumnos


app.config.from_object(DevConfig)
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def index():
        usuario_form = UserForm(request.form)
        # all_alumnos = Alumnos.query.all()
        if request.method == 'POST':
                print("Metodo POST")
                try:
                        alumno = Alumnos(nombre=usuario_form.nombre.data, apaterno=usuario_form.a_paterno.data, email=usuario_form.email.data)
                        db.session.add(alumno)
                        db.session.commit()
                        print("Alumno guardado")
                except Exception as e:
                        print(f"Error en la base de datos: {e}")
                        db.session.rollback()                         
        return render_template('index.html', form=usuario_form)

@app.route('/ABC_Completo', methods=['GET', 'POST'])
def Abc():
        alum = Alumnos.query.all()
        return render_template('ABC_Completo.html', alum=alum)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
        create_form = UserForm(request.form)
        if request.method == 'GET':
                id = request.args.get('id')
                alumno = Alumnos.query.filter_by(id=id).first()
                create_form.id.data = request.args.get('id')
                create_form.nombre.data = alumno.nombre
                create_form.a_paterno.data = alumno.apaterno
                create_form.email.data = alumno.email
        if request.method == 'POST':
                try:
                        id = create_form.id.data
                        alumno = Alumnos.query.filter_by(id=id).first()
                        db.session.delete(alumno)
                        db.session.commit()
                        print("Alumno eliminado")
                except Exception as e:
                        print(f"Error en la base de datos: {e}")
                        db.session.rollback()
                return redirect('/ABC_Completo')
        return render_template('eliminar.html', form=create_form)

@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
        create_form = UserForm(request.form)
        if request.method == 'GET':
                id = request.args.get('id')
                alumno = Alumnos.query.filter_by(id=id).first()
                create_form.id.data = request.args.get('id')
                create_form.nombre.data = alumno.nombre
                create_form.a_paterno.data = alumno.apaterno
                create_form.email.data = alumno.email
        if request.method == 'POST':
                try:
                        id = create_form.id.data
                        alumno = Alumnos.query.filter_by(id=id).first()
                        alumno.nombre = create_form.nombre.data
                        alumno.apaterno = create_form.a_paterno.data
                        alumno.email = create_form.email.data
                        db.session.commit()
                        print("Alumno modificado")
                except Exception as e:
                        print(f"Error en la base de datos: {e}")
                        db.session.rollback()
                return redirect('/ABC_Completo')
        return render_template('modificar.html', form=create_form)
                
                

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
        # titulo = "UTL!!!"
        # nombres = ["Mario", "Juan", "Pedro", "Dario"]
        # return render_template('alumnos.html', titulo=titulo, nombres=nombres)
        usuario_form = UserForm(request.form)
        nombre = None
        p_apellido = None
        m_apellido = None
        edad = None
        email = None
        if request.method == 'POST' and usuario_form.validate():
                nombre = usuario_form.nombre.data
                m_apellido = usuario_form.a_materno.data
                p_apellido = usuario_form.a_paterno.data
                edad = usuario_form.edad.data
                email = usuario_form.email.data

                print(f"Nombre: {nombre} {p_apellido} {m_apellido} Edad: {edad} Email: {email}")

                msj_flash = f"Bienvenido {g.nombre}"
                flash(msj_flash)
        return render_template('alumnos.html', form=usuario_form, nombre=nombre, p_apellido=p_apellido , m_apellido=m_apellido, edad=edad, email=email if email else "Email")
		

@app.errorhandler(404)
def error(error):
		return render_template('404.html', error = error), 404
   


if __name__ == '__main__':
        csrf.init_app(app)
        db.init_app(app)            
        with app.app_context():
                db.create_all()
        app.run(debug=True)
