# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo
from model import Problem

# -- Initialization section --
app = Flask(__name__)

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event": "Avery's Birthday", "date":"2019-07-03"}
    ]

# name of database
# app.config['MONGO_DBNAME'] = 'Test'

# URI of database
# app.config['MONGO_URI'] = 'mongodb+srv://Admin:7EOYAJDMHjJxySMX@cluster0.ydm5p.mongodb.net/Test?retryWrites=true&w=majority'

# mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/sendName', methods=['GET', 'POST'])
def Name():
    if request.method == "GET":
        return "Awesome!"
    else:
        nickname = request.form['nickname']
        return render_template('homepage.html', nickname=nickname)

@app.route('/signUp')
def SignUp():
    return render_template("signup.html")

@app.route('/logIn')
def LogIn():
    return render_template("login.html")

@app.route('/calendar')
def Calendar():
    return render_template("calendar.html")

@app.route('/forum')
def Forum():
    return render_template("forum.html")

@app.route('/interpreter')
def Interpreter():
    return render_template("interpreter.html")

@app.route('/articles-resources')
def Resources():
    return render_template("resources.html")

@app.route('/event/new')
def NewEvent():
    return render_template("new_event.html")

# @app.route('/about-us')
# def AboutUs():
#     return render_template("aboutus.html")

@app.route('/chatback', methods=['GET', 'POST'])
def ChatBack():
    if request.method == "POST":
        problem = request.form['problem']
        cool = Problem(problem)
        name = request.form['name']
        return render_template("chatback.html", cool=cool, name=name)
    else:
        render_template("calendar.html")
