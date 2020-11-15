from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class BloodPressureForm(FlaskForm):
    name = StringField('Username',
                       validators=[DataRequired(), Length(min=2, max=20)])
    systolic_level = IntegerField('systolic_level',
                                  validators=[DataRequired(), NumberRange(min=70, max=190)])
    diastolic_level = IntegerField('diastolic_level',
                                   validators=[DataRequired(), NumberRange(min=40, max=100)])
    submit = SubmitField('Calculate Blood Pressure')

