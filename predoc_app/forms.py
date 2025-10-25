from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, StringField, PasswordField, \
    SubmitField, BooleanField, SelectField, DateField, \
    SelectMultipleField, widgets, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional
from .model import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=10)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=10)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username already exists.')


    def validate_email(self, email):
        result = User.query.filter_by(email = email.data).first()

        if result:
            raise ValidationError('Email already exists.')


class LoginForm(FlaskForm):
    email = StringField("Email: ",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password: ",
                             validators=[DataRequired(), Length(min=10)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PersonalDetailsForm(FlaskForm):
    heights = ['3ft 0in', '3ft 1in', '3ft 2in', '3ft 3in', '3ft 4in', '3ft 5in', '3ft 6in', '3ft 7in',
               '3ft 8in', '3ft 9in', '3ft 10in', '3ft 11in', '4ft 0in', '4ft 1in', '4ft 2in',
               '4ft 3in', '4ft 4in', '4ft 5in', '4ft 6in', '4ft 7in', '4ft 8in', '4ft 9in', '4ft 10in',
               '4ft 11in', '5ft 0in', '5ft 1in', '5ft 2in', '5ft 3in', '5ft 4in', '5ft 5in',
               '5ft 6in', '5ft 7in', '5ft 8in', '5ft 9in', '5ft 10in', '5ft 11in', '6ft 0in', '6ft 1in',
               '6ft 2in', '6ft 3in', '6ft 4in', '6ft 5in', '6ft 6in', '6ft 7in', '6ft 8in',
               '6ft 9in', '6ft 10in', '6ft 11in', '7ft 0in', '7ft 1in', '7ft 2in', '7ft 3in', '7ft 4in',
               '7ft 5in', '7ft 6in', '7ft 7in', '7ft 8in', '7ft 9in', '7ft 10in', '7ft 11in']

    country_code_list = ['+1', "+86", '+81', '+49', '+91', '+44', '+33', '+39', '+1', '+55']

    full_name = StringField("Full Name: ",
                            validators=[DataRequired()])
    dob = DateField("Date of Birth: ", format='%Y-%m-%d',
                    validators=[DataRequired()])
    gender = StringField("Gender: ",
                         validators=[DataRequired()])
    country_code = SelectField('Country Code: ', choices=[(code, code) for code in country_code_list],
                               validators=[DataRequired()])
    contact_number = StringField("Contact Number: ",
                                 validators=[DataRequired()])
    address = StringField('Address: ',
                            validators=[DataRequired()])
    blood_group = StringField('Blood Group: ',
                              validators=[DataRequired()])
    height = SelectField('Height: ', choices=[(height, height) for height in heights],
                         validators=[DataRequired()])
    weight = IntegerField("Weight (in Kg): ",
                          validators=[DataRequired()])
    submit = SubmitField('Update')



class LifestyleForm(FlaskForm):
    smoking_choice = SelectField('Smoking: ', choices=['Yes', 'No'],
                                 validators=[DataRequired()])
    alcohol_use = SelectField('Alcohol consumption: ', choices=['Yes', 'No'],
                              validators=[DataRequired()])
    substance_use = SelectField('Any Carcinogenic Substance intake: ', choices=['Yes', 'No'],
                                validators=[DataRequired()])
    exercise = SelectField('Exercise Frequency: ', choices=['Daily', 'Weekly', 'Rarely', 'No exercise routine'],
                           validators=[DataRequired()])
    sleep_hours = IntegerField('How much hours you sleep(Average): ',
                               validators=[DataRequired()])
    diet_pattern = SelectField('What type of diet pattern you follow: ', choices=['Veg', 'Non-Veg', 'Vegan'],
                               validators=[DataRequired()])
    submit = SubmitField('Update')



class MedicalHistoryForm(FlaskForm):
    diabetes_types = ['Type 1 Diabetes', 'Type 2 Diabetes', 'Gestational Diabetes',
                      'Prediabetes', 'Monogenic Diabetes', 'Latent Autoimmune Diabetes in Adults (LADA) or Type 1.5 Diabetes',
                      'Type 3c Diabetes', 'Steroid-Induced Diabetes', 'Cystic Fibrosis Diabetes',
                      'Wolfram Syndrome', 'Type 5 Diabetes (Malnutrition-related Diabetes)', 'Secondary Diabetes', 'No']

    hypertension_types = ['Secondary Hypertension', 'Resistant Hypertension', 'Isolated Systolic Hypertension',
                          'Malignant Hypertension', 'White Coat Hypertension', 'Masked Hypertension', 'Hypertensive Emergency/Urgency', 'No']

    cardiac_disease_types = ['Coronary Artery Disease', 'Heart Failure', 'Arrhythmias', 'Heart Valve Problems',
                             'Cardiomyopathy', 'Congenital Heart Disease', 'Pericardial Disease', 'Rheumatic Heart Disease', 'No']

    respiratory_types = ['Asthma', 'Chronic Obstructive Pulmonary Disease (COPD)', 'Bronchitis',
                         'Pneumonia', 'Lung Cancer', 'Tuberculosis (TB)', 'Occupational respiratory diseases',
                         'Pulmonary Fibrosis', 'Cystic Fibrosis', 'No']

    diabetes = SelectField("Diabetes: ", choices=[(diab, diab) for diab in diabetes_types],
                           validators=[DataRequired()])
    hypertension = SelectField('Hypertension: ', choices=[(tension, tension) for tension in hypertension_types],
                               validators=[DataRequired()])
    cardiac_disease = SelectField('Any Cardiac disease: ', choices=[(cardiac, cardiac) for cardiac in cardiac_disease_types],
                                  validators=[DataRequired()])
    respiratory_disease = SelectField('Any Respiratory disease: ', choices=[(respiratory, respiratory) for respiratory in respiratory_types],
                                      validators=[DataRequired()])
    epilepsy = SelectField("Epilepsy: ", choices=['Yes', 'No'],
                           validators=[DataRequired()])
    mental_health_condition = StringField('Any Mental Health conditions: ',
                                            validators=[DataRequired()])
    past_surgeries = SelectField('Any Past Surgeries: ', choices=['Yes', 'No'],
                                 validators=[DataRequired()])
    past_surgeries_type = StringField('If yes, which surgery you had: ')

    family_history = SelectMultipleField('Family History of Diseases: ', choices=[
        ('diabetes', 'Diabetes'),
        ('hypertension', 'Hypertension (High BP)'),
        ('cardiac', 'Heart Disease'),
        ('cancer', 'Cancer'),
        ('mental', 'Mental Health Issues (Depression, Anxiety, etc.)'),
        ('asthma', 'Asthma'),
        ('none', 'None')
    ], option_widget=widgets.CheckboxInput(),
    widget=widgets.ListWidget(prefix_label=False))

    submit = SubmitField('Update')



class AllergiesForm(FlaskForm):
    allergy_type_options = ['Food Allergy', 'Drug/Medication Allergy', 'Insect Allergy', "Pet Allergy",
                            'Environmental Allergy', 'Latex Allergy', 'Skin Allergy', 'Respiratory Allergy / Asthma',
                            'Skin allergies', 'Eye Allergy', 'Severe Reaction']

    allergy_status = SelectField('Any kind of allergy: ', choices=['Yes', 'No'],
                                 validators=[DataRequired()])


    allergy_type = SelectField('Type of allergy: ', choices=[(allergy, allergy) for allergy in allergy_type_options])


    allergy_triggers = StringField("What causes my allergy")

    allergy_reaction = StringField('What is the allergy reaction: ')

    add_more = SubmitField('Add More')
    next = SubmitField('Next')


class CurrentMedicationForm(FlaskForm):
    medication = SelectField('Any medications undergoing: ', choices=['Yes', 'No'],
                             validators=[DataRequired()])
    drug_name = StringField('Which medicines are you taking: ')
    dosage = StringField('What is the dosage of each Drug: ')
    frequency = StringField('What is the frequency of intake of each drug: ')
    start_date = DateField("Start date: ", format='%Y-%m-%d',
                        validators=[Optional()])
    end_date = DateField('When will the prescription end: ', format='%Y-%m-%d',
                        validators=[Optional()])

    add_more = SubmitField('Add More')
    next = SubmitField('Next')


class AccidentsForms(FlaskForm):
    accident_type_list = ['Road Accidents', 'Slips, Trips, and Falls', 'Workplace Accidents',
                          'Medical Accidents', 'Home Accidents', 'Sports and Recreation', 'Natural Disasters',
                          'Vehicle and Bicycle Accidents', 'No']

    injured_body_part = ['Head', 'Chest', 'Abdomen', 'Spine', 'Limb', 'Eye', 'Other', 'None']

    accident_problem = ['Pain', 'Stiffness', 'Weakness', 'Vision issues', 'Breathing issues', 'None']


    any_accident = SelectField('Have you ever had a medical-treated injury/accident?',
                               choices=['Yes', 'No'], validators=[DataRequired()])

    accident_date = DateField('Approximate date/year of accident', format='%Y-%m-%d', validators=[Optional()])

    accident_type = SelectField('Type of accident', choices=[(acci_type, acci_type) for acci_type in accident_type_list],
                                validators=[Optional()])

    body_part_injured = SelectField('Main body part injured', choices=[(injury, injury) for injury in injured_body_part],
                                validators=[Optional()])

    hospitalized = SelectField('Were you hospitalized?', choices=['Yes', 'No'],
                                validators=[Optional()])

    any_surgey = SelectField('Any surgery/implants from the accident?', choices=['Yes', 'No'],
                                validators=[Optional()])

    lasting_problem = SelectField('Any current problems from this injury?', choices=[(accident, accident) for accident in accident_problem],
                                validators=[Optional()])

    reports_available = SelectField('Do you have reports ?', choices=['Yes', 'No'],
                                validators=[Optional()])

    add_more = SubmitField('Add More')
    next = SubmitField('Next')


class ChooseDiseaseForm(FlaskForm):
    dermat = SubmitField('Dermat')
    oral = SubmitField('Oral')


class DermatSymptomDescription(FlaskForm):
    skin_issue = StringField('What skin issue are you experiencing?')
    affected_body_parts = StringField('Which part(s) of your body are affected?')
    noticing_time = StringField('When did you first notice it?')
    area_affected = StringField('Is the affected area spreading or staying in one place?')
    fluid = StringField('Do you see any scaling, pus, or fluid?')
    next = SubmitField('Next')


class Dermat_Medical_and_lifestyle_history(FlaskForm):
    condition = StringField('Did this condition appear after using a new product (soap, cream, detergent, etc.)?')
    allergies = StringField('Do you have any known allergies?')
    history = StringField('Any history of eczema, psoriasis, or fungal infections?')
    family = StringField('Does anyone in your family have similar skin conditions?')
    hormonal = StringField('Do you have hormonal issues, diabetes, or thyroid disorder?')
    next = SubmitField('Next')


class Dermat_Severity_and_progression(FlaskForm):
    scale = IntegerField('On a scale of 1–10, how severe is your itching or irritation?')
    situation_worsening = StringField('How does the condition behave throughout the day (e.g., worse in morning/evening/after activity)?',choices=['Yes', 'No'])
    hormonal = StringField('Describe any sensations you feel — for example, burning, tightness, tingling, or pain.')
    conditions = StringField('How has the condition changed over time — is it improving, worsening, or staying the same?')
    next = SubmitField('Next')


class Dermat_habits_and_hygiene(FlaskForm):
    sunscreen = StringField('How often do you use moisturizer or sunscreen?')
    exposure = SelectField('Do you have prolonged sun or chemical exposure at work?', choices=['Yes', 'No'])
    bathing = SelectField('Do you maintain daily skin hygiene (bathing, exfoliation, etc.)?', choices=['Yes', 'No'])
    medications = TextAreaField('Please describe any creams, ointments, or medications you’re currently using for this condition (mention how long you’ve been using them).')
    next = SubmitField('Next')


class OralSymptomDescription(FlaskForm):
    Symptoms = StringField('What oral issue are you facing? (pain, bleeding gums, ulcers, discoloration, swelling, etc.)')
    areas = StringField('Which area is affected? (tooth, gums, tongue, cheek, lips)')
    startof_problem = StringField('When did the problem start?')
    sensitivity = StringField('Is there pain or sensitivity while eating hot/cold food?')
    smell = SelectField('Do you notice any bad smell or taste?', choices=['Yes', 'No'])
    next = SubmitField('Next')


class Oral_Medical_and_lifestyle_history(FlaskForm):
    dental = StringField('Have you had any recent dental procedures (fillings, cleaning, extraction)?')
    chronic = SelectField('Do you have any chronic condition?', choices=['Yes', 'No'])
    medications = StringField('Are you taking any medication that causes dry mouth or swelling?')
    family = StringField('Any family history of gum or tooth disease?')
    next = SubmitField('Next')


class Oral_Severity_and_progression(FlaskForm):
    scale = IntegerField('On a scale of 1–10, how severe is your pain or discomfort?')
    pain = StringField('Describe when the pain or irritation occurs most — for example, while chewing, after meals, or randomly.')
    condition = StringField('How has the condition changed over time — is it improving, worsening, or staying about the same?')
    issues = StringField('Describe any associated issues you notice, such as swelling, bleeding, or difficulty opening your mouth.')
    next = SubmitField('Next')


class Oral_habits_and_hygiene(FlaskForm):
    brush = StringField('How often do you brush your teeth each day?')
    floss = SelectField('Do you use floss or mouthwash regularly?', choices=['Yes', "No"])
    sugary = StringField('How often do you consume sugary foods or drinks?')
    last_checkup = StringField('When was your last dental checkup?')
    next = SubmitField('Next')




class UpdateAffectedPhoto(FlaskForm):
    picture = FileField('Please upload a clear image of the affected area (use front camera, natural lighting if possible).', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')










