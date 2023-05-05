from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'jfheuheuhhdkjd8d77877d8ffd7s666f6d6f7dfdsf'



@app.route('/')
def home():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html', count=session['count'])

@app.route('/reset')
def destroy():
    session['count'] = 0
    return redirect('/')

# @app.route('/count')
# def count():
#     session['count'] += 1
#     return redirect('index.html', count=count)





if __name__ == '__main__':
    app.run(debug=True)