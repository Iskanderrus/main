import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "black", "purple", "orange"]
y_coordinate = [-70, -40, -10, 20, 50, 80]

for turtle_number in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_number])
    tim.setposition(x=-230, y=y_coordinate[turtle_number])


while tim.xcor() < 500:
    tim.forward(random.randint(5, 15))

screen.exitonclick()
