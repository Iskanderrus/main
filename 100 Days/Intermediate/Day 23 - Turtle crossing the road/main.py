import random
import time
import colorgram
from turtle import Screen
from cars import Car
from crosser import Crosser
#from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Import colors for the cars

#imported_colors = colorgram.extract('images/image.jpg', 20)


# for color in imported_colors:
#     rgb = color.rgb
#     color_red = rgb.r
#     color_green = rgb.g
#     color_blue = rgb.b
#     color = (color_red, color_green, color_blue)
#     colors_list.append(color)
# print(colors_list)

# Add y coordinates for the running cars

cars = Car()
crosser = Crosser()
# Introducing controls:
screen.listen()
screen.onkeypress(crosser.up, "Up")


cars_list = []
game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()

    cars_list.append(cars.create_manager())
    for car in cars_list:
        cars.move()

screen.exitonclick()
