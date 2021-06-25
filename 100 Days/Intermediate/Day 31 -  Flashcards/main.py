from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Armenian Letter")
    canvas.itemconfig(card_word, text=current_card["Armenian Letter"])




window = Tk()
window.title("հայերեն")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 158, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="WORD", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png", width=100, height=99)
unknown_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png", width=100, height=99)
unknown_button = Button(image=check_image, highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=1)


next_card()



window.mainloop()
