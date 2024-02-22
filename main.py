from flask import Flask, render_template, request
from forms import UserForm
from flask import flash 
from flask import g
from flask_wtf.csrf import CSRFProtect
from config import DevConfig, Config
app = Flask(__name__)
app.config.from_object(DevConfig)

csrf = CSRFProtect(Config)


@app.route('/')
def index():
	return render_template('index.html')

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
	app.run(debug=True)