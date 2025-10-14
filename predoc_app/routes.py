from flask import render_template, flash, redirect, url_for, request, abort, send_file
from .forms import RegistrationForm, LoginForm, PersonalDetailsForm, \
                    LifestyleForm, MedicalHistoryForm, AllergiesForm, \
                        CurrentMedicationForm, UpdateProfilePhoto, AccidentsForms
from predoc_app import app, bcrypt, db
from .model import User
from flask_login import login_user, current_user, logout_user, login_required
from .utils import generate_primary_key_SQL, gender_code, height_converter, calculate_bmi,\
                    clear_country_code_input, connectDb, connectMongoDB, generate_primary_key_Mongo
import os
import io
import pdfkit
import secrets


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

    conn, curr = connectDb()

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

    conn, curr = connectDb()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)

            if request.args.get('next'):
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))

            return redirect(url_for('profile'))

        else:
            flash('Login unsuccessful! check username and password', 'danger')
    return render_template('login.html', form = form, css_file = 'register.css')





@app.route('/personal-details', methods = ['GET', 'POST'])
@login_required
def personal_details():
    form = PersonalDetailsForm()

    conn, curr = connectDb()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        curr.execute('''INSERT INTO personal_details (personal_id, user_id, full_name, date_of_birth, gender, contact_country_code, contact_number, address, blood_group, height_cm, weight_kg, bmi)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''', (generate_primary_key_SQL('personal_details',conn, curr),
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

    conn, curr = connectDb()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        curr.execute('''INSERT INTO lifestyle (lifestyle_id, user_id, smoking_status, alcohol_use, substance_use, exercise_frequency, sleep_hours, diet_pattern)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s);''', (generate_primary_key_SQL('lifestyle',conn,curr), user_id, form.smoking_choice.data,
                                                            form.alcohol_use.data, form.substance_use.data, form.exercise.data,
                                                            form.sleep_hours.data, form.diet_pattern.data,))

        conn.commit()

        return redirect(url_for('medical_details'))

    return render_template('lifestyle_details.html', form=form)





@app.route('/medical_details', methods = ['GET', 'POST'])
@login_required
def medical_details():
    form = MedicalHistoryForm()

    conn, curr = connectDb()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        family_history = ','.join(form.family_history.data)

        curr.execute('''INSERT INTO medical_history (medical_id, user_id, diabetes, hypertension, cardiac_disease, respiratory_disease, epilepsy, mental_health_condition, past_surgeries, past_surgeries_type, family_history)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''', (generate_primary_key_SQL('medical_history', conn, curr), user_id, form.diabetes.data,
                                                                    form.hypertension.data, form.cardiac_disease.data, form.respiratory_disease.data, form.epilepsy.data,
                                                                    form.mental_health_condition.data, form.past_surgeries.data, form.past_surgeries_type.data,
                                                                    family_history,))

        conn.commit()

        return redirect(url_for('allergy_details'))

    return render_template('medical_history.html', form = form)






allergies_details = []
@app.route('/allergy-details', methods = ['GET', 'POST'])
@login_required
def allergy_details():
    form = AllergiesForm()
    db = connectMongoDB()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        if form.add_more.data:
            new_allergy = {
                "allergy_type": form.allergy_type.data,
                "allergy_name": form.allergy_triggers.data,
                "allergy_reaction": form.allergy_reaction.data
            }

            allergies_details.append(new_allergy)

            return redirect(url_for('allergy_details'))

        elif form.next.data:
            if form.allergy_status.data == 'Yes' and len(allergies_details) == 0:
                db['allergy'].insert_one({"allergy_id":generate_primary_key_Mongo('allergy', db), "user_id":user_id, "allergyStatus": True,
                                          "allergy_details":[{"allergy_type":form.allergy_type.data, "allergy_name":form.allergy_triggers.data, "allergy_reaction":form.allergy_reaction.data}]})

            elif form.allergy_status.data == 'Yes' and len(allergies_details) > 0:
                new_allergy = {
                    "allergy_type": form.allergy_type.data,
                    "allergy_name": form.allergy_triggers.data,
                    "allergy_reaction": form.allergy_reaction.data
                }

                allergies_details.append(new_allergy)
                db['allergy'].insert_one({"allergy_id":generate_primary_key_Mongo('allergy', db), "user_id":user_id, "allergyStatus": True,
                                          "allergy_details":allergies_details})

            else:
                db['allergy'].insert_one({"allergy_id":generate_primary_key_Mongo('allergy', db), "user_id":user_id, "allergyStatus": False})

            return redirect(url_for('current_medication_details'))

    return render_template('allergy_details.html', form = form)





current_medication = []
@app.route('/current-medication-details', methods = ['GET', 'POST'])
@login_required
def current_medication_details():
    form = CurrentMedicationForm()

    db = connectMongoDB()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if form.validate_on_submit():

        if form.add_more.data:
            medication_details = {
                'medicineName': form.drug_name.data,
                'dosage': form.dosage.data,
                'frequency': form.frequency.data,
                'start_date': form.start_date.data,
                'end_date': form.end_date.data
            }

            current_medication.append(medication_details)
            return redirect(url_for('current_medication_details'))

        elif form.next.data:
            if form.medication.data == 'Yes' and len(current_medication) == 0:
                db['medication'].insert_one({'medicationId':generate_primary_key_Mongo('medication', db), 'user_id': user_id,
                                             'medicationStatus':True, 'medicationDetails':[{'medicineName': form.drug_name.data,
                                             'dosage': form.dosage.data, 'frequency': form.frequency.data, 'start_date': form.start_date.data,
                                             'end_date': form.end_date.data}]})

            elif form.medication.data == 'Yes' and len(current_medication) > 0:
                medication_details = {
                    'medicineName': form.drug_name.data,
                    'dosage': form.dosage.data,
                    'frequency': form.frequency.data,
                    'start_date': form.start_date.data,
                    'end_date': form.end_date.data
                }

                current_medication.append(medication_details)
                db['medication'].insert_one({'medicationId':generate_primary_key_Mongo('medication', db), 'user_id': user_id,
                                'medicationStatus':True,'medicationDetails':medication_details})

            else:
                db['medication'].insert_one({'medicationId':generate_primary_key_Mongo('medication', db), 'user_id': user_id,
                                'medicationStatus':False})
            return redirect(url_for('accident_details'))

    return render_template('current_medication.html', form=form)




accident_details_list = []
@app.route('/accident-details', methods=['GET', 'POST'])
@login_required
def accident_details():
    forms = AccidentsForms()

    db = connectMongoDB()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    if forms.validate_on_submit():
        if forms.add_more.data:
            accident_report = {
                'accidentDate':forms.accident_date.data,
                'type':forms.accident_type.data,
                'bodypartInjured':forms.body_part_injured.data,
                'Hospitalized':forms.hospitalized.data,
                'Surgery':forms.any_surgey.data,
                'CurrentProblems':forms.lasting_problem.data,
                'ReportStatus':forms.reports_available.data
            }

            accident_details_list.append(accident_report)
            return redirect(url_for('accident_details'))

        elif forms.next.data:
            if forms.any_accident.data == "Yes" and len(accident_details_list) == 0:
                db['accidents'].insert_one({'accidentId': generate_primary_key_Mongo('accidents', db), 'user_id': user_id,
                                            'accidentStatus': True, 'accidentdetails': [{
                                                                        'accidentDate':forms.accident_date.data,
                                                                        'type':forms.accident_type.data,
                                                                        'bodypartInjured':forms.body_part_injured.data,
                                                                        'Hospitalized':forms.hospitalized.data,
                                                                        'Surgery':forms.any_surgey.data,
                                                                        'CurrentProblems':forms.lasting_problem.data,
                                                                        'ReportStatus':forms.reports_available.data
                                                                    }]})

            elif forms.any_accident.data == "Yes" and len(accident_details_list) > 0:
                accident_report = {
                    'accidentDate':forms.accident_date.data,
                    'type':forms.accident_type.data,
                    'bodypartInjured':forms.body_part_injured.data,
                    'Hospitalized':forms.hospitalized.data,
                    'Surgery':forms.any_surgey.data,
                    'CurrentProblems':forms.lasting_problem.data,
                    'ReportStatus':forms.reports_available.data
                }

                accident_details_list.append(accident_report)

                db['accidents'].insert_one({'accidentId': generate_primary_key_Mongo('accidents', db), 'user_id': user_id,
                                            'accidentStatus': True, 'accidentdetails': accident_details_list})

            else:
                db['accidents'].insert_one({'accidentId': generate_primary_key_Mongo('accidents', db), 'user_id': user_id,
                                            'accidentStatus': False})

            return redirect(url_for('generate_medical_report'))

    return render_template('accident.html', form = forms)






@app.route("/generate_medical_report")
@login_required
def generate_medical_report():
    if current_user.is_authenticated:
        user_id = current_user.user_id

    conn, curr = connectDb()

    curr.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
    users = curr.fetchone()

    curr.execute('SELECT * FROM personal_details WHERE user_id = %s ORDER BY created_at', (user_id,))
    personal = curr.fetchone()

    curr.execute('SELECT * FROM lifestyle WHERE user_id = %s ORDER BY created_at', (user_id,))
    lifestyle = curr.fetchone()

    curr.execute('SELECT * FROM medical_history WHERE user_id = %s ORDER BY created_at', (user_id,))
    medical = curr.fetchone()

    curr.execute('SELECT * FROM allergies WHERE user_id = %s ORDER BY created_at', (user_id,))
    allergies = curr.fetchall()

    curr.execute('SELECT * FROM current_medication_details WHERE user_id = %s ORDER BY created_at', (user_id,))
    current_medication = curr.fetchall()

    curr.execute('SELECT * FROM accidents WHERE user_id = %s ORDER BY created_at', (user_id,))
    accidents = curr.fetchall()

    html_content = render_template('report.html', users = users, personal=personal, lifestyle=lifestyle,
                                   medical=medical, allergies=allergies, current_medication=current_medication, accidents=accidents)

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltox\bin\wkhtmltopdf.exe'
    # path_wkhtmltopdf = "/usr/bin/wkhtmltopdf"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    pdf_bytes = pdfkit.from_string(html_content, False, configuration=config)

    curr.execute('INSERT INTO report(report_id, user_id, file_path) VALUES(%s, %s, %s)', (generate_primary_key_SQL('report', conn, curr),
                                                                                          user_id, pdf_bytes))

    conn.commit()
    flash("Check downloads! Your Report is available there.")
    return redirect(url_for('profile'))







@app.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():

    conn, curr = connectDb()

    if current_user.is_authenticated:
        user_id = current_user.user_id

    form = UpdateProfilePhoto()

    if form.validate_on_submit():
        if form.picture.data:
            random_hex = secrets.token_hex(8)
            _, f_ext = os.path.splitext(form.picture.data.filename)
            picture_fn = random_hex + f_ext
            picture_path = os.path.join(app.root_path, 'static/images/profile_pics', picture_fn)
            form.picture.data.save(picture_path)
            picture_file = picture_fn
            current_user.profile_photo = picture_file

            return redirect(url_for('profile'))


    # curr.execute('SELECT * FROM personal_details WHERE user_id = %s ORDER BY created_at LIMIT 1', (user_id,))
    # user_details = curr.fetchone()

    image_file = url_for('static', filename = 'images/profile_pics/' + current_user.profile_photo)

    # return render_template('new_profile.html', user_details=user_details,
    return render_template('new_profile.html',
                           image_file=image_file, css_file = 'profile.css', form=form)

    return render_template('new_profile.html', )






@app.route('/generate_report')
@login_required
def generate_report():

    return redirect(url_for('personal_details'))






@app.route('/downloads')
@login_required
def make_downloads():
    if current_user.is_authenticated:
        user_id = current_user.user_id

    conn, curr = connectDb()

    curr.execute('SELECT report_id, file_path, created_at FROM report WHERE user_id = %s ORDER BY created_at', (user_id,))
    file_paths = curr.fetchall()

    return render_template('downloads.html', file_paths=file_paths, css_file = 'downloads.css')






@app.route("/download/<string:report_id>")
def download(report_id):

    conn, curr = connectDb()

    curr.execute("SELECT file_path FROM report WHERE report_id = %s", (report_id,))
    row = curr.fetchone()

    if not row:
        abort(404, "Report not found")

    pdf_bytes = row[0]   # BYTEA column comes as bytes in Python

    # Return as downloadable file
    return send_file(
        io.BytesIO(pdf_bytes),
        as_attachment=True,
        download_name=f"{report_id}.pdf",
        mimetype="application/pdf"
    )






@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
