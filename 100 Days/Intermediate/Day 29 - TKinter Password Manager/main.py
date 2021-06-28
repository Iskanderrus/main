from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
import datetime as dt


now = dt.datetime.today().strftime("%d/%m/%y")
# ---------------------------- SEARCH FUNCTION ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("../../../../../Документы/password_manager_log.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Ups...", message=f"No data file exist.")

    else:
        if website in data:
            messagebox.showinfo(title=f"{website} is found!", message=f"Password for user:\n{data[website]['username']}"
                                                                      f"\ncopied to clipboard")
            pyperclip.copy(data[website]['password'])  # --> copy to clipboard
        else:
            messagebox.showerror(title="Ups...", message=f"No details for {website} exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def password_creator():
    password_entry.delete(0, END)  # --> cleanup the password entry if something was there occasionally
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(numbers) for _ in range(randint(2, 4))] + \
                    [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)  # --> display the new password in GUI
    pyperclip.copy(password)  # --> copy to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def log_saver():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
            "logged_date": now,
        }
    }

    if len(website) <= 4 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Entry Error", message="Ups... Please don't leave any blank fields!")
    else:
        try:
            with open("../../../../../Документы/password_manager_log.json", "r") as file:
                # reading from the json file
                data = json.load(file)
                # updating data in the old version of the json file
                data.update(new_data)

            with open("../../../../../Документы/password_manager_log.json", "w") as file:
                # updating the json file with the updated data
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            with open("../../../../../Документы/password_manager_log.json", "w") as file:
                # updating the json file with the updated data
                json.dump(new_data, file, indent=4)
        website_entry.delete(4, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Create App window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

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
generate_button = Button(text="Generate Password", height=1, highlightthickness=0, font=("Arial", 10),
                         command=password_creator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=44, font=("Arial", 10), command=log_saver)
add_button.grid(column=1, row=4, columnspan=2)

add_button = Button(text="Search", highlightthickness=0, width=16, font=("Arial", 10), command=find_password)
add_button.grid(column=2, row=1)

add_button = Button(text="EXIT", highlightthickness=0, width=16, font=("Arial", 10), command=window.destroy)
add_button.grid(column=2, row=5)

# Add entries
website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()  # --> cursor will be placed into this field after launching the app
website_entry.insert(0, "www.")

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "alex_ru2002@list.ru")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

window.mainloop()
