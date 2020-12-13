from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError


class BloodPressureForm(FlaskForm):
    name = StringField('Username',
                       validators=[DataRequired(), Length(min=2, max=20)])
    systolic_level = IntegerField('systolic_level',
                                  validators=[DataRequired(), NumberRange(min=70, max=190)])
    diastolic_level = IntegerField('diastolic_level',
                                   validators=[DataRequired(), NumberRange(min=40, max=100)])
    submit = SubmitField('Calculate Blood Pressure')

    def validate_diastolic_level(self, diastolic_level):
        if self.systolic_level.data < diastolic_level.data:
            raise ValidationError(
                f"Systolic Level must be higher than Diastolic Level"
            )
