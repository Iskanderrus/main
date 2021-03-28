# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
valid_sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(valid_sum)


#BMI Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(int(int(weight) / float(height) ** 2))


# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
difference = 90 - int(age)
in_days = difference * 365
in_weeks = difference * 52
in_months = difference * 12

print(f'You have {in_days} days, {in_weeks} weeks and {in_months} months left.')


greeting = "Welcome to tip calculator"
print(greeting)
bill = float(input("What was the total bill& $"))
tips = int(input("What percentage tip would you like to give& 10, 12 or 15? "))
people = int(input("How many people want to split the bill? "))
part = bill * (1 + tips / 100) / people
print(f"Each person should pay: ${round(part, 2)}")
