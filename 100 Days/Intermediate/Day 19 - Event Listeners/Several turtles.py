import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "grey", "purple", "orange"]
y_coordinate = [-70, -40, -10, 20, 50, 80]
all_turtles = []
winning_color = []

for turtle_number in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_number])
    new_turtle.setposition(x=-230, y=y_coordinate[turtle_number])
    all_turtles.append(new_turtle)

while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Wrong input. Enter a color: ")
else:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
if user_bet == winning_color:
    print(f"You win. {winning_color.title()} turtle won the race.")
else:
    print(f"You lose. {winning_color.title()} turtle was the first in this race.")
screen.exitonclick()
