
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route('/')
def home():
    if 'user_id' in session:
        redirect('/dashboard')
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(data)
    return render_template('dashboard.html', logged_user=logged_user)

@app.route('/user/logout')
def logout():
    del session['user_id']
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def log_user():
    data = {
        'email': request.form['email']
    }
    potential_user = User.get_by_email(data)
    if not potential_user:
        flash('invalid credentials', 'log')
        return redirect('/')
    if not bcrypt.check_password_hash(potential_user.password, request.form['password']):
        flash('invalid credentials', 'log')
        return redirect('/')
    session['user_id'] = potential_user.id
    session['user_fname'] = potential_user.first_name
    return redirect('/dashboard')

# ----------------------------------------------------- REGISTER / REDIRECT
@app.route('/user/register', methods=['POST'])
def reg_user():
    if not User.validation(request.form):
        return redirect('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        **request.form,
        # "username": request.form['username'],
        "password" : pw_hash,
        'confirm_password': pw_hash
    }
    # Call the save @classmethod on User
    logged_user_id = User.save(data)
    # store user id into session
    session['user_id'] = logged_user_id
    session['user_fname'] = request.form['first_name']
    
    return redirect("/dashboard")

