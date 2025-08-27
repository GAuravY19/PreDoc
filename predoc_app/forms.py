from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, \
    SubmitField, BooleanField, SelectField, DateField, \
    TextAreaField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username: ',
                           validators=[DataRequired(), Length(min=6, max=10)])
    email = StringField("Email: ",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password: ",
                             validators=[DataRequired(), Length(min=10)])
    confirm_password = PasswordField('Confirm Password: ',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


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

    full_name = StringField("Full Name: ",
                            validators=[DataRequired()])
    dob = DateField("Date of Birth: ", format='%Y-%m-%d',
                    validators=[DataRequired()])
    gender = StringField("Gender: ",
                         validators=[DataRequired()])
    contact_number = StringField("Contact Number: ",
                                 validators=[DataRequired(), Length(min=10,max=10)])
    address = TextAreaField('Address: ',
                            validators=[DataRequired()])
    blood_group = StringField('Blood Group: ',
                              validators=[DataRequired()])
    height = SelectField('Height: ', choices=heights,
                         validators=[DataRequired()])
    weight = IntegerField("Weight (in Kg): ",
                          validators=[DataRequired()])


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


class MedicalHistoryForm(FlaskForm):
    diabetes_types = ['Type 1 Diabetes', 'Type 2 Diabetes', 'Gestational Diabetes',
                      'Prediabetes', 'Monogenic Diabetes', 'Latent Autoimmune Diabetes in Adults (LADA) or Type 1.5 Diabetes',
                      'Type 3c Diabetes', 'Steroid-Induced Diabetes', 'Cystic Fibrosis Diabetes',
                      'Wolfram Syndrome', 'Type 5 Diabetes (Malnutrition-related Diabetes)', 'Secondary Diabetes', 'No']

    hypertension_types = ['Secondary Hypertension', 'Resistant Hypertension', 'Isolated Systolic Hypertension',
                          'Malignant Hypertension', 'White Coat Hypertension', 'Masked Hypertension', 'Hypertensive Emergency/Urgency', 'No']

    cardiac_disease_types = ['Coronary Artery Disease', 'Heart Failure', 'Arrhythmias', 'Heart Valve Problems',
                             'Cardiomyopathy', 'Congenital Heart Disease', 'Pericardial Disease', 'Rheumatic Heart Disease']

    respiratory_types = ['Asthma', 'Chronic Obstructive Pulmonary Disease (COPD)', 'Bronchitis',
                         'Pneumonia', 'Lung Cancer', 'Tuberculosis (TB)', 'Occupational respiratory diseases',
                         'Pulmonary Fibrosis', 'Cystic Fibrosis', 'No']

    diabetes = SelectField("Diabetes: ", choices=diabetes_types,
                           validators=[DataRequired()])
    hypertension = SelectField('Hypertension: ', choices=hypertension_types,
                               validators=[DataRequired()])
    cardiac_disease = SelectField('Any Cardiac disease: ', choices=cardiac_disease_types,
                                  validators=[DataRequired()])
    respiratory_disease = SelectField('Any Respiratory disease: ', choices=respiratory_types,
                                      validators=[DataRequired()])
    epilepsy = SelectField("Epilepsy: ", choices=['Yes', 'No'],
                           validators=[DataRequired()])
    mental_health_condition = TextAreaField('Any Mental Health conditions: ',
                                            validators=[DataRequired()])
    past_surgeries = SelectField('Any Past Surgeries: ', choices=['Yes', 'No'],
                                 validators=[DataRequired()])
    past_surgeries_type = TextAreaField('If yes, which surgery you had: ')

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


class AllergiesForm(FlaskForm):
    allergy_type_options = ['Food allergies', 'Drug (medication) allergies', 'Insect allergies',
                            'Pet allergies', 'Mold allergies', 'Pollen allergies', 'Latex allergies',
                            'Skin allergies', 'Allergic asthma', 'Eye allergies (allergic conjunctivitis)',
                            'Anaphylaxis']

    allergy_name_options = ['Milk allergy', 'Egg allergy', 'Peanut allergy', 'Tree nut allergy (e.g., walnuts, almonds, cashews)',
                    'Shellfish allergy (e.g., shrimp, lobster, crab)', 'Fish allergy', 'Soy allergy', 'Wheat allergy',
                    'Sesame allergy', 'Pollen allergy', 'House dust mite allergy', 'Pet dander allergy (cats and dogs)',
                    'Mold allergy', 'Insect allergy', 'Drug allergies (e.g., penicillin)', 'Latex allergy',
                    'Nickel allergy (contact dermatitis from jewelry and metals)', 'Perfume/cosmetic allergies']

    allergy_status = SelectField('Any kind of allergy: ', choices=['Yes', 'No'],
                                 validators=[DataRequired()])
    allergy_type = SelectMultipleField('Type of allergy: ', choices=allergy_type_options)
    allergy_name = SelectMultipleField("Allergy Name: ", choices=allergy_name_options)
    allergy_reaction = TextAreaField('What is the allergy reaction: ')


class CurrentMedicationForm(FlaskForm):
    medication = SelectField('Any medications undergoing: ', choices=['Yes', 'No'],
                             validators=[DataRequired()])
    drug_name = TextAreaField('Which medicines are you taking: ')
    dosage = TextAreaField('What is the dosage of each Drug: ')
    frequency = TextAreaField('What is the frequency of intake of each drug: ')
    start_date = DateField("Start date: ", format='%Y-%m-%d')
    end_date = DateField('When will the prescription end: ', format='%Y-%m-%d')


