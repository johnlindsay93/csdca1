from flask import Flask, render_template, url_for, flash, redirect
from forms import BloodPressureForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '191153e08901f4a4dd20a8af12052fe6'

posts = [
    {
        'name' : 'john',
        'systolic_level': '130',
        'diastolic_level': 60
    }
]


@app.route('/', methods=['GET', 'POST'])
def home():
    form = BloodPressureForm()
    if form.validate_on_submit():
        flash(f'Info Submitted for calculation for {form.name.data}!', 'Success')
    return render_template('home.html', posts=posts, form=form)

if __name__=='__main__':
    app.run()
