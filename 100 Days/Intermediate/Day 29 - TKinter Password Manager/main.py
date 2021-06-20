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
canvas.create_image(125, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Add labels
website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=("Arial", 10))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(column=0, row=3)


# Add buttons
generate_button = Button(text="Generate Password", highlightthickness=0, font=("Arial", 10))
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=44, font=("Arial", 10))
add_button.grid(column=1, row=4, columnspan=2)

# Add entries
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

window.mainloop()
