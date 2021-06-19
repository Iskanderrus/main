from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create Canvas
canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
background_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=background_image)
canvas.create_text(110, 143, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.pack()

window.mainloop()
