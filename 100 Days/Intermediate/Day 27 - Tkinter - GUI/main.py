import tkinter as tk


window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="This is a label", font=("Arial", 24, "italic")) # --> creating a component
my_label.pack(expand=True) # --> run the component









window.mainloop()