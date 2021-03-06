from flask import Flask, render_template, url_for, flash, redirect, request
from forms import BloodPressureForm
from calculations import Calculations
from graph import generate_gauge
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

app.secret_key = b'ksdfglbvlsdfbos'
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = BloodPressureForm()
    calculations = Calculations()
    if form.validate_on_submit():
        flash(f'Info Submitted for calculation for {form.name.data}!', 'Success')
        flash(f'Your current blood pressure is:')
        systolic_level = int(request.form.get("systolic_level"))
        diastolic_level = int(request.form.get("diastolic_level"))
        gauge = generate_gauge(systolic_level, diastolic_level)
        result = calculations.calculate_blood_pressure(systolic_level, diastolic_level)
        return render_template('result.html', value=result, form=form, chart=gauge)
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run()
