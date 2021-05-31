from turtle import Turtle, colormode
import random

colormode(255)

colors_list = [(245, 239, 230), (227, 235, 243), (247, 230, 238), (124, 180, 210), (234, 243, 238), (198, 174, 16),
               (29, 119, 167), (176, 14, 45), (235, 150, 76), (236, 204, 90), (217, 124, 163), (26, 144, 74),
               (215, 80, 123), (9, 171, 210), (212, 61, 27), (237, 77, 45), (245, 157, 187), (64, 21, 53),
               (12, 183, 150), (13, 31, 75)]
y_coordinate = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()

    def create_manager(self):
        for _ in y_coordinate:
            self.setposition(x=260, y=random.choice(y_coordinate))
            self.color(random.choice(colors_list))
            self.setheading(180)

    def move(self):
        self.forward(random.randint(0, 40))
