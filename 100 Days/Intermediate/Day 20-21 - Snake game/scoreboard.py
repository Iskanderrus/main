from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = -1
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 280)
        self.text = "Счёт: "

    def board_refresh(self):
        self.clear()
        self.counter += 1
        self.write(self.text + str(self.counter), align=ALIGNMENT, font=FONT)
