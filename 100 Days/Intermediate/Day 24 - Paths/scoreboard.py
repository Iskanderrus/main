from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = -1
        self.penup()
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)

    def reset(self):
        if self.counter > self.high_score:
            self.high_score = self.counter
        self.counter = -1
        self.board_refresh()

    def board_refresh(self):
        """
        Function to clean the scoreboard of the game and assign the new score.
        :return: None
        """
        self.clear()
        self.counter += 1
        self.write(f"Счёт: {self.counter}. Наивысший балл: {self.high_score}.", align=ALIGNMENT, font=FONT)
