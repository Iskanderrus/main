import tkinter as tk


window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="Хочешь попасть в Америку?", font=("Arial", 24, "italic")) # --> creating a component
my_label.pack() # --> run the component


# Button

def button_clicked():
    my_label.config(text="Поступай служить\nв ракетные войска!")


button = tk.Button(text="ДА!", command=button_clicked)
button.pack()

# Entry
my_input = tk.Entry()
my_input.insert(1, string="Номер телефона")
my_input.pack()






window.mainloop()