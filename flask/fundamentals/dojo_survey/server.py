from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = "Keep your secrets"

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/info', methods=['POST'])       #---------Home-------
def info():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['course'] = request.form['course']
    # -------------------------------checks if clicked if not returns empty string----
    if 'front_end' in request.form and request.form['front_end'] != '':
        session['front_end'] = request.form['front_end']
    else: 
        session['front_end'] = ''
    # -------------------------------checks if clicked if not returns empty string----
    if 'back_end' in request.form and request.form['back_end'] != '':
        session['back_end'] = request.form['back_end']
    else: 
        session['back_end'] = ''
    if session['back_end'] and session['front_end'] != '':
        choice = session['front_end'] + session['back_end']
    session['comments'] = request.form['comments']
    return redirect('/result')

# ----------------------------------------------- Loads new page with results----
@app.route('/result')
def result():
    if session['back_end'] and session['front_end'] != '':
        choice = session['front_end'] + ' and ' + session['back_end']
    elif session['back_end'] != '':
        choice = session['back_end']
    elif session['front_end'] != '':
        choice = session['front_end']
    return render_template('result.html', choice = choice)






if __name__ == '__main__':
    app.run(debug=True)