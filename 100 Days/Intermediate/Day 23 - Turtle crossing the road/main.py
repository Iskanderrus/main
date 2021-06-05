import time
from turtle import Screen

from cars import CarManager
from crosser import Crosser
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=630, height=620)
screen.tracer(0)
screen.title("Черепаха на дороге")

crosser = Crosser()
car_manager = CarManager()
# Introducing controls:
screen.listen()
screen.onkeypress(crosser.up, "Up")
scoreboard = Scoreboard()

game_is_on = True
game_speed = 0.1
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision

    for car in car_manager.all_cars:
        if crosser.distance(car) < 20:
            game_is_on = False
            screen.clear()
            scoreboard.game_over()

    # Score counter
    if crosser.ycor() > 280:
        crosser.go_to_start()
        scoreboard.add_point()
        screen.update()
        game_speed *= 0.9

screen.exitonclick()
