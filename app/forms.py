from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from .models import User 


class RegisterForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("passowrd")])
    submit = SubmitField("Cadastrar")

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first
        if user:
            raise ValidationError("Este nome de usuário já existe. Por favor, escolha outro")