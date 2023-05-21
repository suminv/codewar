def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    elif bmi > 30:
        return "Obese"


assert bmi(50, 1.80) == "Underweight"
assert bmi(80, 1.80) == "Normal"
assert bmi(90, 1.80) == "Overweight"
assert bmi(110, 1.80) == "Obese"
assert bmi(50, 1.50) == "Normal"
