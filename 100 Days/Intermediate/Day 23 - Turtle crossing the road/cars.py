from turtle import Turtle, colormode
import random

colormode(255)

colors_list = [(124, 180, 210), (198, 174, 16),
               (29, 119, 167), (176, 14, 45), (235, 150, 76), (236, 204, 90), (217, 124, 163), (26, 144, 74),
               (215, 80, 123), (9, 171, 210), (212, 61, 27), (237, 77, 45), (245, 157, 187), (64, 21, 53),
               (12, 183, 150), (13, 31, 75)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(colors_list))
            random_y = random.randint(-230, 220)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
