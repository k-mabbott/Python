
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja


@app.route('/ninjas')
def show():
    all_dojos = Dojo.get_all_dojos()
    return render_template('ninja_new.html', all_dojos=all_dojos)


@app.route('/ninja/create', methods=['POST'])
def new_ninja():
    print(request.form)
    Ninja.save(request.form)

    return redirect(f"/dojos/{request.form['dojo_id']}")
