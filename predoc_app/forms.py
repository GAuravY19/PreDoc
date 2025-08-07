from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username: ',
                           validators=[DataRequired(), Length(min=6, max=10)])
    email = StringField("Email: ",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password: ",
                             validators=[DataRequired(), Length(min=10)])
    confirm_password = PasswordField('Confirm Password: ',
                                     validators=[DataRequired(), EqualTo('pasword')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    pass

class DetailsForm(FlaskForm):
    pass
