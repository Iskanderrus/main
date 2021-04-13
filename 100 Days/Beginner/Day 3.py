#Ticket machine

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("Wat is your age? "))
    if age < 12:
        price = 5
    elif age <= 18:
        price = 7
    elif 45 <= age <= 55:
        price = 0
    else:
        price = 12
    photo = input("Do yo want to take a photo? Y or N.")
    if photo == "Y":
        if price == 0:
            print(f"You don't pay for your ticket but we charge $3 for photo. Total price: ${price + 3}.")
        elif price == 5:
            print(f"You pay ${price} for Child ticket and $3 for photo. Total price: ${price + 3}.")
        elif price == 7:
            print(f"You pay ${price} for Youth ticket and $3 for photo. Total price: ${price + 3}.")
        elif price == 12:
            print(f"You pay ${price} for Adult ticket and $3 for photo. Total price: ${price + 3}.")
    else:
            print(f"Your price is: ${price}")
else:
    print("Please eat better to grow faster. See you when you would reach 120 cm.")





#