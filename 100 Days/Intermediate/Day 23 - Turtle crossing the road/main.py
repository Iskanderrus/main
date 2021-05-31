import random
import colorgram
from turtle import Turtle, Screen, colormode
from cars import Car
from crosser import Crosser

colormode(255)
screen = Screen()
screen.setup(width=800, height=600)


# Import colors for the cars

imported_colors = colorgram.extract('images/image.jpg', 20)
colors_list = []

for color in imported_colors:
    rgb = color.rgb
    color_red = rgb.r
    color_green = rgb.g
    color_blue = rgb.b
    color = (color_red, color_green, color_blue)
    colors_list.append(color)
print(colors_list)
# Add y coordinates for the running cars

y_coordinate = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140]

all_cars = []
for car in y_coordinate:
    new_car = Car(y_position=car, color=random.choice(colors_list))
    new_car.penup()
    all_cars.append(new_car)

crosser = Crosser()
counter = 0
while counter < 100:
    for car in all_cars:
        car.move()

screen.exitonclick()
