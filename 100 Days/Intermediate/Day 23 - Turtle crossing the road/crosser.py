from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
INITIAL_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Crosser(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("black")
        self.go_to_start()

    def go_to_start(self):
        self.goto(INITIAL_POSITION)

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)
