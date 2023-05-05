from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'jfheuheuhhdkjd8d77877d8ffd7s666f6d6f7dfdsf'



@app.route('/')
def home():
    if 'page_visits' in session:
        session['page_visits'] += 1
    else:
        session['page_visits'] = 1
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html', count=session['count'])


@app.route('/destroy_session')
def destroy():
    session['count'] = 0
    session['page_visits'] = 0
    return redirect('/')


@app.route('/double')
def count_double():
    session['count'] += 1
    return redirect('/')


@app.route('/custom_count', methods=['POST'])
def custom():
    print(request.form)
    # session['count_number'] = request.form['count_number']
    # print(request.form['count_number'])
    session['count'] += int(request.form['count_number'])-1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)