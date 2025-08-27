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
        flash(f'Account created for {form.username.data}!', 'success')

        return redirect(url_for('login'))

    return render_template('register.html', form=form, css_file = 'register.css')



@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'gaurav@gmail.com' and form.password.data == 'gaurav1234':
            flash('You have been logged in!', 'success')
            return redirect('home')

        else:
            flash('Login unsuccessful! check username and password', 'danger')
    return render_template('login.html', form = form, css_file = 'login.css')



@app.route('/profile')
def profile():
    return "<h1> profile Page </h1>"

@app.route("/logout")
def logout():
    return "<h1> Logout page </h1>"
