

class Calculations:

    def calculate_blood_pressure(self, systolic_level, diastolic_level):
        if systolic_level < 90 and diastolic_level < 60:
            bloodpressure = "Low"
        elif 90 <= systolic_level < 120 and diastolic_level < 80:
            bloodpressure = "Ideal -ideal"
        elif 120 <= systolic_level < 140 or 80 <= diastolic_level < 90:
            bloodpressure = "Pre-High"
        elif systolic_level > 140 or diastolic_level > 90:
            bloodpressure = "High"
        return bloodpressure
