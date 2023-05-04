from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '182b9bdd22ab9ed4d12e236c78gfcb9a393ec15f71bbf5dc987d54727823bcbf'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print(request.form['name'])
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect("/show")

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")





if __name__ == '__main__':
    app.run(debug=True)