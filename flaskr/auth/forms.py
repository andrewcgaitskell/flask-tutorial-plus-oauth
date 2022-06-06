from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Length

class GithubForm(FlaskForm):
    login = SubmitField('Log in with Github')
