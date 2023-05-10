from flask import Flask, render_template, request, redirect, session 
import random


app = Flask(__name__)
app.secret_key = "Keep your secrets"


@app.route('/')
def home():
    session['random_num'] = random.randint(0, 100)
    session['count'] = 0
    print(session['random_num'])
    return render_template('index.html')



@app.route('/guess', methods=['POST'])
def guess(): 
    session['count'] += 1
    session['user_guess'] = request.form['user_guess']
    if session['user_guess'] == '':
        return redirect('/was_it_right')
    print(request.form)
    return redirect('/was_it_right')


@app.route('/was_it_right')
def was_it_right():
    # if session['user_guess'] == '':
    #     return redirect('/was_it_right')
    user_guess = session['user_guess']
    if user_guess != '':
        user_guess = int(user_guess)
    else: 
        user_guess = -1
    return render_template('guess.html', user_guess=user_guess)





if __name__ == '__main__':
    app.run(debug=True)