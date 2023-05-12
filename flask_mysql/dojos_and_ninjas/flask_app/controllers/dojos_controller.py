
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


# --------------------------------------------HOME PAGE / CREATE

@app.route('/')
@app.route('/dojos')
def show_all_dojos():

    return render_template('dojos.html', all_dojos=Dojo.get_all_dojos() )

# -------------------------------------------- FORM REDIRECT ROUTE
@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    
    Dojo.save(request.form)
    return redirect('/dojos')

# -------------------------------------------- SHOW ONE DOJO WITH ALL NINJAS
@app.route('/dojos/<int:id>')
def show_all_ninjas_in_dojo(id):
    print('\n\n\n**' , id)
    data = {'id': id}
    dojo_with_ninjas = Dojo.get_all_ninjas(data)
    return render_template('dojos_ninjas.html', dojo_with_ninjas=dojo_with_ninjas)


