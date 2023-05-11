
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User


# --------------------------------SHOW ALL
@app.route('/users')
def show_all_users():

    return render_template("show_all.html", all_users=User.get_all())

# --------------------------------SHOW ONE
@app.route('/user/<int:id>')
def show_one_user(id):
    data = {
        'id': id
    }
    print(User.get_one(data))
    one_user = User.get_one(data)[0]
    return render_template('show_one.html', one_user=one_user)



# --------------------------------ADD USER / Redirect
@app.route('/users/create', methods=['POST'])
def create_user():
    id = User.save(request.form)
    print(id)
    return redirect(f'/user/{id}')

# --------------------------------ADD USER / render
@app.route('/users/new')
def new_user():
    
    return render_template('new_user.html')

# --------------------------------DELETE USER
@app.route('/delete_user/<int:id>')
def delete_user(id):
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/users')


# --------------------------------EDIT USER
@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = {
        'id': id
    }
    one_user = User.get_one(data)[0]
    print(one_user)
    return render_template('edit_user.html', one_user=one_user)


@app.route('/users/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        'id': id ,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print(data)
    User.update(data)
    return redirect(f"/user/{id}")
# one_user = User.update(data)


