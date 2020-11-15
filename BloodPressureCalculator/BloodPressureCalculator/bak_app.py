from BloodPressureCalculator import BloodPressureCalculator


def main():
    calculator = BloodPressureCalculator()
    value1 = calculator.get_user_diastolic_level()
    value2 = calculator.get_user_systolic_info()

    result = calculator.verify_values(value2, value1)

    if result == True:
        print("True")
    else:
        print("Exception")

if __name__ == '__main__':
    main()
