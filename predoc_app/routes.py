from flask import render_template, flash, redirect, url_for, request
from .forms import RegistrationForm, LoginForm, PersonalDetailsForm
from predoc_app import app, bcrypt, curr, conn, db
from .model import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/start-home')
def start_home():
    return "<h1> Start Home </h1>"



@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(username = form.username.data,
                    email = form.email.data, password_hash = hashed_pw)

        db.session.add(user)
        db.session.commit()
        flash(f'Account created. You can now login!', 'success')

        return redirect(url_for('login'))

    return render_template('register.html', form=form, css_file = 'register.css')



@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page) if next_page else redirect(url_for('home'))

        else:
            flash('Login unsuccessful! check username and password', 'danger')
    return render_template('login.html', form = form, css_file = 'login.css')


@app.route('/personal_details')
@login_required
def personal_details():
    form = PersonalDetailsForm()

    return render_template('personal_details.html', form=form)



















@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
