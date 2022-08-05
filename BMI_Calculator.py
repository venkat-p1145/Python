weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in m): "))

bmi = weight / (height * height)
value = ""

if bmi < 18.5:
    value = "underweight"
elif 18.5 < bmi < 25:
    value = "normal weight"
elif 25 < bmi < 30:
    value = "overweight"
elif 30 < bmi < 35:
    value = "Moderately obese"
elif 35 < bmi < 40:
    value = "Severely obese"
elif bmi >= 40:
    value = "Very severely obese"

print(f"Result is you are {value}.")
