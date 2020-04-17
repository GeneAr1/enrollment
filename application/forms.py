from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User


class Loginform(FlaskForm):
    email       =   StringField("Email", validators=[DataRequired(), Email()])
    password    =   PasswordField("Password", validators=[DataRequired(), Length(min=6,max=20)])
    remember_me =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")


class RegisterForm(FlaskForm):
    email               =   StringField("Email", validators=[DataRequired(), Email()])
    password            =   PasswordField("Password", validators=[DataRequired(), Length(min=6,max=20)])
    password_confirm    =   PasswordField("Password Confirm", validators=[DataRequired(), Length(min=6,max=20), EqualTo('password')])
    first_name          =   StringField("First Name", validators=[DataRequired(), Length(min=2,max=50)])
    last_name           =   StringField("Last Name", validators=[DataRequired(), Length(min=2, max=50)])
    submit              =   SubmitField("Register Now")


#email validation module
    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use.  Please use different email")
