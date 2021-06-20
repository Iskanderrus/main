from tkinter import *
import math

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #

# Create App window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Create Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Add labels
# timer_label = Label(text="Timer", font=("Chilanka", 30, "bold"), bg=YELLOW, fg=GREEN)
# timer_label.grid(column=1, row=0)
#
# checkmark_label = Label(font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
# checkmark_label.grid(column=1, row=3)
#
# # Add buttons
# start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
# start_button.grid(column=0, row=2)
#
# reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
# reset_button.grid(column=2, row=2)

window.mainloop()
