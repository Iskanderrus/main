height = input("What is your height in m: ")
weight = input("What is your weight in kg: ")

bmi = float(weight) / float(height) ** 2

if bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)}. You are underweight. Eat more often.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi, 2)}. Congratulations! You have ideal weight. Keep good job!")
elif bmi < 30:
    print(f"Your BMI is {round(bmi, 2)}. Sorry to inform, but looks like you have some overweight. Make sport in the morning!")
elif bmi < 35:
    print(f"Your BMI is {round(bmi, 2)}. Hey there!!! Stop eating!!! You are obese!")
else:
    print(f"Your BMI is {round(bmi, 2)}. You are clinically obese. Stop eating and go to doctor...")
