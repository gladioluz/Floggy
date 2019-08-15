from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SelectField, StringField, DateField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Почта', [DataRequired(), Length(max=128)])
    password = PasswordField('Пароль', [DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')
