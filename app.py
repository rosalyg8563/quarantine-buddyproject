# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template ("index.html")

@app.route('/happy')
def happy():
    return render_template("happy.html")

@app.route('/bored')
def bored():
    return render_template("bored.html")

@app.route('/sad')
def sad():
    return render_template("sad.html")

@app.route('/angry')
def angry():
    return render_template("angry.html")

@app.route('/mission')
def mission():
    return render_template("mission.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/home')
def home():
    return render_template("index.html")


