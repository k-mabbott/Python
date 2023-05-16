
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app import DB
from flask_app.models.user_model import User
from flask_app.models.friend_model import Friend


@app.route('/')
def homepage():
    all_users = User.get_all()
    all_friends = Friend.get_all_friendship()
    return render_template('index.html', all_users=all_users, all_friends=all_friends)

@app.route('/save_friendship', methods=['POST'])
def save_new_friendship():
    if not Friend.validation(request.form):
        return redirect('/')
    new_user = Friend.save_friend(request.form)
    return redirect('/')