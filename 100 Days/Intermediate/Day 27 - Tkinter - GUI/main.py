import tkinter as tk


window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
background_image = tk.PhotoImage("../Day 25 - CSV Files/US States Game/blank_states_img.gif")
background_label = tk.Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label
my_label = tk.Label(text="Хочешь попасть в Америку?", font=("Arial", 24, "italic")) # --> creating a component
my_label.pack() # --> run the component


# Button


def button_clicked():
    my_label.config(text="Поступай служить \nв ракетные войска!")


button = tk.Button(text="ДА!", command=button_clicked)
button.pack()




window.mainloop()