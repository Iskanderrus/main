import random
import time
from turtle import Screen
from cars import CarManager
from crosser import Crosser
#from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


crosser = Crosser()
car_manager = CarManager()
# Introducing controls:
screen.listen()
screen.onkeypress(crosser.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if crosser.distance(car) < 20:
            game_is_on = False





screen.exitonclick()
