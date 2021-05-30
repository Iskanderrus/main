from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Screen settings:
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Пинг-Понг")
screen.tracer(0)

# Introducing main parts of the game:
left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

# Introducing controls:
screen.listen()
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

# Main game cycle:
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the upper or lower wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles:
    if ball.distance(right_paddle) < 65 and ball.xcor() == 360 or \
            ball.distance(left_paddle) < 65 and ball.xcor() == -360:
        ball.bounce_x()

    # Detect right paddle missing the ball:
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.refresh()

    # Detect left paddle missing the ball:
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.refresh()


screen.exitonclick()
