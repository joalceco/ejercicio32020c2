from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Ejercicio3Form(FlaskForm):
    palabra1 = StringField('Palabra 1', validators=[DataRequired()])
    palabra2 = StringField('Palabra 2', validators=[DataRequired()])
    submit = SubmitField('Submit')

