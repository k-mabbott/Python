from flask import Flask, render_template, request, redirect

app = Flask(__name__)

    # http://localhost:5000 - should display 8 by 8 checkerboard
    # http://localhost:5000/4 - should display 8 by 4 checkerboard
    # http://localhost:5000/(x)/(y) - should display x by y 
    # checkerboard.  For example, http://localhost:5000/10/10 should 
    # display 10 by 10 checkerboard.  Before you pass x or y to Jinja, 
    # please remember to convert it to integer first (so that you can 
    # use x or y in a for loop)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print(request.form['name'])
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')







if __name__ == '__main__':
    app.run(debug=True)