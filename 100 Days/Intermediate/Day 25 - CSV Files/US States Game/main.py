import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# Getting mouse click coordinates
# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)

states_full_list = pd.read_csv("50_states.csv")
states = states_full_list['state'].to_list()
used_names = []
while len(used_names) < 50:
    answer_state = screen.textinput(title=f"{len(used_names)}/ 50 Guess the state", prompt="What's another state name?")
    if answer_state.title() not in used_names:
        if answer_state.title() in states:
            choice = states_full_list[states_full_list.state == answer_state.title()]
            state = turtle.Turtle()
            state.hideturtle()
            state.penup()
            state.goto(int(choice["x"]), int(choice["y"]))
            state.write(answer_state.title(), align="center", font=("Courier", 7, "bold"))
            used_names.append(answer_state.title())


turtle.mainloop()
