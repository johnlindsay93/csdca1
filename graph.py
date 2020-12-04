import pygal
from pygal import style

def generate_gauge(systolic, diastolic):
    gauge = pygal.SolidGauge(
        half_pie=True, inner_radius=0.70,
        style=pygal.style.styles['default'](value_font_size=10),
        height=150, width=400)

    gauge.add('Systolic', [{'value': systolic, 'max_value': 190}])
    gauge.add('Diastolic', [{'value': diastolic, 'max_value': 100}])
    return gauge.render_data_uri()
