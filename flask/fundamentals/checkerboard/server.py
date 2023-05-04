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
def playground():
    return render_template("index.html", x=8, y=8)

@app.route('/<int:x>')
def play(x):
    return render_template("index.html", x=x, y=8)

@app.route('/<int:x>/<int:y>')
def board_size(x, y):
    return render_template("index.html", x=x, y=y)
# @app.route('/play/<int:num>/<string:color>')
# def play_with_colors(num, color):
#     return render_template("index.html", num=num, color=color)
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def board_colors(x, y, color1, color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)










if __name__ == '__main__':
    app.run(debug=True)