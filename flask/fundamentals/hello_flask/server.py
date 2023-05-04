from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
# app.run(debug=True, host="localhost", port=8000)
# change from port 5000 to 8000 if port is busy
def hello_world():
    return render_template("index.html")

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:var>')
def say(var):
    return f"Hi {var.capitalize()}!!"

@app.route('/repeat/<int:num>/<string:var>')
def repeat(num, var):
    return f"{var * num} \n"

@app.route('/hello/<string:variable>/<int:num>')
def hello_again(variable, num):
    return render_template("hello.html", variable= variable, num= num)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)






@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__ == '__main__':
    app.run(debug=True)