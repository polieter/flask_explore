from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LoginForm(FlaskForm):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired(),
                                          validators.InputRequired()])
