from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app import DB
from flask_app.models.user_model import User
from flask_app.models.friend_model import Friend



@app.route('/save_user', methods=['POST'])
def save_new_user():
    if not User.validation(request.form):
        return redirect('/')
    new_user = User.save(request.form)
    return redirect('/')



