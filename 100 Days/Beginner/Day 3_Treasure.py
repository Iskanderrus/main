
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossing = input("You are on the cross road. Do you want to go right or left? left or right: \n")
if crossing.lower() == "right":
    print("Goblins smashed you... Game over :-(")
else:
    print("You arrived to the lake.")
    lake = input("Do you wait for the boat or swim? wait or swim: \n")
    if lake.lower() == "swim":
        print("Lake is full of alligators. You had no chance... Game over :-(")
    else:
        print("You crossed the lake and arrived to an old castle.")
        castle = input("You see three doors in front of you. Which one would you choose: red, yellow or blue? \n")
        if castle.lower() == "red" or castle.lower() == "blue":
            print("This was a trap. Game over.")
        else:
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')