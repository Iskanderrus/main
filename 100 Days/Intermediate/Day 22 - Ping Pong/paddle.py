from turtle import Turtle

STARTING_POSITION = (-380, 0)
MOVE_DISTANCE = 18
UP = 90
DOWN = 270


class Paddle:

    def __init__(self):
        self.paddle = Turtle("square")
        self.create_paddle(STARTING_POSITION)

    def create_paddle(self, position):
        self.paddle.penup()
        self.paddle.color("green")
        self.paddle.setposition(position)

    def up(self):
        self.paddle.setheading(UP)
        if self.paddle.ycor() < 300:
            self.paddle.forward(MOVE_DISTANCE)

    def down(self):
        self.paddle.setheading(DOWN)
        if self.paddle.ycor() > -300:
            self.paddle.forward(MOVE_DISTANCE)
