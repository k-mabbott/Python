from flask import Flask, render_template

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
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", users = users)












if __name__ == '__main__':
    app.run(debug=True)