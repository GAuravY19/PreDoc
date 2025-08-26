from flask import render_template, flash, redirect, url_for
from .forms import RegistrationForm, LoginForm
from dotenv import load_dotenv
import os
import psycopg2
from predoc_app import app, bcrypt

load_dotenv()

conn = psycopg2.connect(host = os.getenv("host"),
                        dbname = os.getenv('db_name'),
                        user = os.getenv('user'),
                        password = os.getenv('password'),
                        port = os.getenv('port'))

curr = conn.cursor()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/start-home')
def start_home():
    return "<h1> Start Home </h1>"

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        curr.execute(f'''INSERT INTO users (username, email, password_hash)
                        VALUES (%s, %s, %s);''', (form.username.data, form.email.data, hashed_pw,))
        conn.commit()
        redirect(url_for('login'))
    return render_template('register.html', form=form, css_file = 'register.css')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form = form, css_file = 'login.css')

@app.route('/profile')
def profile():
    return "<h1> profile Page </h1>"

@app.route("/logout")
def logout():
    return "<h1> Logout page </h1>"
