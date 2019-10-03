from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, Optional, Length, NumberRange
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

responsaveis = [
        ('', ''),
        ('José', 'José'), #_('José')
        ('Carlos', 'Carlos'),
        ('Maria', 'Maria'),
        ('João', 'João'),       
    ]
class ItemForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    number = IntegerField('Código', validators=[DataRequired(), NumberRange(min=1000, max=9999)])
    qtt = IntegerField('Quantidade', validators=[DataRequired(), NumberRange(min=1)])
    responsavel = SelectField('Responsável', choices=responsaveis, validators=[DataRequired()])
    retornar = BooleanField('Retornar')
    #validators=[ Optional(), Length(min=8, max=35)]
    #password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    name = StringField('')
    responsavel = SelectField('Responsável', choices=responsaveis)
    submit = SubmitField('Submit')