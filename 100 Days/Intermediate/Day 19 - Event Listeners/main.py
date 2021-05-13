from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")


def move_forwards():
    tim.forward(10)


def move_back():
    tim.backward(10)


def turn_left():
    tim.left(2)


def turn_right():
    tim.right(2)


def clear():
    tim.clear()
    tim.reset()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
