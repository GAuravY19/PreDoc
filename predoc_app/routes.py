from flask import render_template
from .app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/start-home')
def start_home():
    return "<h1> Start Home </h1>"

@app.route("/register")
def register():
    return "<h1> Register Page </h1>"

@app.route("/login")
def login():
    return "<h1> Login Page </h1>"

@app.route('/profile')
def profile():
    return "<h1> profile Page </h1>"

@app.route("/logout")
def logout():
    return "<h1> Logout page </h1>"
