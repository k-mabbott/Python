from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = "Keep your secrets"

@app.route('/')
def home():

    return render_template('index.html')


@app.route('/process_money')
def process_money():
    pass






if __name__ == '__main__':
    app.run(debug=True)