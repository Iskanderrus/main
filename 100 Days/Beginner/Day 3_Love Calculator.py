print("Welcome to the Love Calculator!")
name1 = input("What is your mane? \n")
name2 = input("What is his or her name? \n")
counter_true = 0
counter_love = 0
name = name1 + name2
for char in name:
    if char.upper() in "TRUE":
        counter_true += 1
for char in name:
    if char.upper() in "LOVE":
        counter_love += 1

percent = int(str(counter_true) + str(counter_love))
if 40 <= percent <= 50:
    print(f"Your score is {percent}, you are alright together.")
elif percent <= 10 or percent >= 90:
    print(f"Your score is {percent}, you go together like coke and Mentos.")
else:
    print(f"Your score is {percent}.")