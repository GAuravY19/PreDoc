from flask import render_template, flash, redirect, url_for, request
from .forms import RegistrationForm, LoginForm, PersonalDetailsForm, \
                    LifestyleForm, MedicalHistoryForm, AllergiesForm, CurrentMedicationForm
from predoc_app import app, bcrypt, curr, conn, db
from .model import User
from flask_login import login_user, current_user, logout_user, login_required
from .utils import generate_primary_key_personal_details, gender_code, height_converter, calculate_bmi,\
                    clear_country_code_input


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


@app.route('/personal-details', methods = ['GET', 'POST'])
@login_required
def personal_details():
    form = PersonalDetailsForm()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        curr.execute('''INSERT INTO personal_details (personal_id, user_id, full_name, date_of_birth, gender, contact_country_code, contact_number, address, blood_group, height_cm, weight_kg, bmi)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''', (generate_primary_key_personal_details(conn, curr),
                                                                            user_id, form.full_name.data,form.dob.data,
                                                                            gender_code(form.gender.data), clear_country_code_input(form.country_code.data),
                                                                            str(form.contact_number.data), str(form.address.data),
                                                                            form.blood_group.data, height_converter(form.height.data),
                                                                            form.weight.data, calculate_bmi(height_converter(form.height.data),form.weight.data),))

        conn.commit()
        return redirect(url_for('lifestyle_details'))

    return render_template('personal_details.html', form=form)


@app.route('/lifestyle_details', methods = ['GET', 'POST'])
@login_required
def lifestyle_details():
    form = LifestyleForm()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        curr.execute('''INSERT INTO lifestyle (lifestyle_id, user_id, smoking_status, alcohol_use, substance_use, exercise_frequency, sleep_hours, diet_pattern)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s);''', (generate_primary_key_personal_details('lifestyle',conn,curr), user_id, form.smoking_choice.data,
                                                            form.alcohol_use.data, form.substance_use.data, form.exercise.data,
                                                            form.sleep_hours.data, form.diet_pattern.data,))

        conn.commit()

        return redirect(url_for('medical_details'))

    return render_template('lifestyle_details.html', form=form)


@app.route('/medical_details', methods = ['GET', 'POST'])
@login_required
def medical_details():
    form = MedicalHistoryForm()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        family_history = ','.join(form.family_history.data)

        curr.execute('''INSERT INTO medical_history (medical_id, user_id, diabetes, hypertension, cardiac_disease, respiratory_disease, epilepsy, mental_health_condition, past_surgeries, past_surgeries_type, family_history)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''', (generate_primary_key_personal_details('medical_history', conn, curr), user_id, form.diabetes.data,
                                                                    form.hypertension.data, form.cardiac_disease.data, form.respiratory_disease.data, form.epilepsy.data,
                                                                    form.mental_health_condition.data, form.past_surgeries.data, form.past_surgeries_type.data,
                                                                    family_history,))

        conn.commit()

        return redirect(url_for('allergy_details'))

    return render_template('medical_history.html', form = form)


@app.route('/allergy-details', methods = ['GET', 'POST'])
@login_required
def allergy_details():
    form = AllergiesForm()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():
        allergy_type = ','.join(form.allergy_type.data)
        allery_name = ','.join(form.allergy_name.data)

        if form.add_more.data:

            curr.execute('''INSERT INTO allergies (allergy_id, user_id, allergy_status, allergy_type, allergy_name, allergy_reaction)
                         VALUES (%s,%s,%s,%s,%s,%s);''', (generate_primary_key_personal_details('allergies', conn, curr), user_id,
                                                          form.allergy_status.data,allergy_type, allery_name,form.allergy_reaction.data))

            conn.commit()
            return redirect(url_for('allergy_details'))

        elif form.next.data:

            curr.execute('''INSERT INTO allergies (allergy_id, user_id, allergy_status, allergy_type, allergy_name, allergy_reaction)
                         VALUES (%s,%s,%s,%s,%s,%s);''', (generate_primary_key_personal_details('allergies', conn, curr), user_id,
                                                          form.allergy_status.data,allergy_type, allery_name,form.allergy_reaction.data))

            conn.commit()
            return redirect(url_for('current_medication_details'))

    return render_template('allergy_details.html', form = form)



@app.route('/current-medication-details', methods = ['GET', 'POST'])
@login_required
def current_medication_details():
    form = CurrentMedicationForm()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        if form.add_more.data:
            curr.execute('''INSERT INTO current_medication_details (medication_id, user_id, medication, drug_name, dosage, frequency, start_date, end_date)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s);''', (generate_primary_key_personal_details('current_medication_details', conn, curr),user_id, form.medication.data,
                         form.drug_name.data,form.dosage.data, form.frequency.data,form.start_date.data, form.end_date.data,))

            conn.commit()

            return redirect(url_for('current_medication_details'))

        elif form.next.data:
            curr.execute('''INSERT INTO current_medication_details (medication_id, user_id, medication, drug_name, dosage, frequency, start_date, end_date)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s);''', (generate_primary_key_personal_details('current_medication_details', conn, curr),user_id, form.medication.data,
                         form.drug_name.data,form.dosage.data, form.frequency.data,form.start_date.data, form.end_date.data,))

            conn.commit()
            return redirect(url_for('profile'))


    return render_template('current_medication.html', form=form)




@app.route('/profile')
@login_required
def profile():
    if current_user.is_authenticated:
        user_id = current_user.user_id

    curr.execute('SELECT date_of_birth, blood_group, height_cm, weight_kg FROM personal_details WHERE user_id = %s', (user_id,))
    user_details = curr.fetchone()

    return render_template('profile.html', user_details=user_details)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
