
from flask import Flask
# DATABASE
DB = 'recipes'

app = Flask(__name__)
app.secret_key = "keep your secrets"