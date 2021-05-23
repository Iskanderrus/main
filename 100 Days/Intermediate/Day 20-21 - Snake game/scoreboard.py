from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = -1
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)
        self.text = "Счёт: "

    def board_refresh(self):
        """
        Function to clean the scoreboard of the game and assign the new score.
        :return: None
        """
        self.clear()
        self.counter += 1
        self.write(self.text + str(self.counter), align=ALIGNMENT, font=FONT)
