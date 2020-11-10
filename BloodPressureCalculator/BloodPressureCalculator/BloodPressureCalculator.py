class BloodPressureCalculator:
    """
    This class calculates the users bloodpressure by taking their systolic
    and diastolic values
    """

    def __init__(self, systolic_high=None, systolic_low=None, diastolic_high=None, diastolic_low=None):
        self.systolic_high = 190
        self.systolic_low = 70
        self.diastolic_high = 100
        self.diastolic_low = 40
        self.bloodpressure: str

    def get_user_systolic_info(self):
        try:
            systolic_level = int(input("Please enter your systolic level here: "))
            if self.systolic_low < systolic_level < self.systolic_high:
                BloodPressureCalculator.user_systolic_level = systolic_level
            else:
                print("Please keep your systolic level within the range of 70 - 190")
            return systolic_level
        except ValueError:
            print("That was not a number. Please enter a positive number")

    def get_user_diastolic_level(self):
        try:
            diastolic_level = int(input("Please enter your diastolic level here: "))
            if self.diastolic_low < diastolic_level < self.diastolic_high:
                BloodPressureCalculator.user_diastolic_level = diastolic_level
            else:
                print("Please keep your diastolic level within the range of 40 - 100")
            return diastolic_level
        except ValueError:
            print("That was not a number. Please enter a positive number")

    @staticmethod
    def verify_values(systolic_level, diastolic_level):
        if systolic_level > diastolic_level:
            return True
        else:
            return Exception

    def calculate_blood_pressure(self, systolic_level, diastolic_level):
        if systolic_level < 90 and diastolic_level < 60:
            self.bloodpressure = "Low"
        elif 90 <= systolic_level < 120 and 60 <= diastolic_level < 80:
            self.bloodpressure = "Ideal"
        elif 120 <= systolic_level < 140 or 80 <= diastolic_level < 90:
            self.bloodpressure = "Pre-High"
        elif systolic_level > 140 or diastolic_level > 90:
            self.bloodpressure = "High"
        return self.bloodpressure




