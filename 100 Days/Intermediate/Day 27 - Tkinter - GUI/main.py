import tkinter as tk


def button_clicked():
    my_label.config(text="Поступай служить\nв ракетные войска!")


window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=800, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tk.Label(text="Хочешь попасть в Америку?", font=("Arial", 24, "italic"))  # --> creating a component
my_label.grid(row=0, column=0)  # --> run the component
my_label.config(padx=30, pady=30)

# Button
button = tk.Button(text="ДА!", command=button_clicked)
button.grid(row=1, column=1)

button2 = tk.Button(text="No!!!")
button2.grid(row=0, column=2)

# Entry
my_input = tk.Entry()
my_input.insert(1, string="Номер телефона")
my_input.grid(row=3, column=3)

window.mainloop()
