from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 280)
        self.text = "Счёт: "

    def board_refresh(self):
        self.write(self.text + str(self.counter), align="center", font=("Arial", 10, "normal"))


