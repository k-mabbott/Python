
from flask import Flask

DB = 'books'

app = Flask(__name__)
app.secret_key = "shhhhhh"