import turtle
import pandas as pd
from state import StateUS
from warning_message import Message
import time

# Create game board with a map of the US
screen = turtle.Screen()
screen.title("US States Game")
image = "../US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Import US states data set
states_full_list = pd.read_csv("../US States Game/50_states.csv")

# Create list of the states
states = states_full_list['state'].to_list()

# Create list of already used state names
used_names = []

# Introduce main components
state = StateUS()
warning = Message()
start_time = time.time()

# Main game logic
while len(used_names) < 50:
    answer_state = screen.textinput(title=f"{len(used_names)}/ 50 Guess the state",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        states_to_learn = pd.DataFrame(states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state not in used_names:
        if answer_state in states:
            choice = states_full_list[states_full_list.state == answer_state]
            state.map_state(answer_state, int(choice["x"]), int(choice["y"]))
            used_names.append(answer_state)
            states.remove(answer_state)
        else:
            text = "There is no state with this name in the U.S.\nTry again."
            warning.write_warning(text)
    else:
        text = f"{answer_state} is on the map already. Try again."
        warning.write_warning(text)

text = f"Congratulations! All States are correctly mapped!\n You did it witin {(time.time() - start_time)}"
warning.write_warning(text)

screen.exitonclick()
