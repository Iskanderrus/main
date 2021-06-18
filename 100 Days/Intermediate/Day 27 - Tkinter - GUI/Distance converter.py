import tkinter as tk


def button_clicked():
    miles = miles_entry.get()
    result.config(text=f"{round(float(miles) * 1.6, 2)}")


window = tk.Tk()
window.title("Mile to km converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=10)

# Entry
miles_entry = tk.Entry()
miles_entry.grid(row=1, column=1)
miles_entry.config(width=10)

# Labels
miles_label = tk.Label(text="Miles", font=("Arial", 12))  # --> creating a component
miles_label.grid(row=1, column=2)  # --> run the component
miles_label.config(padx=30, pady=10)

label_2 = tk.Label(text="is equal to", font=("Arial", 12))  # --> creating a component
label_2.grid(row=2, column=0)  # --> run the component
label_2.config(padx=30, pady=10)

result = tk.Label(text="0", font=("Arial", 12))  # --> creating a component
result.grid(row=2, column=1)  # --> run the component
result.config(padx=60, pady=10)

km_label = tk.Label(text="Km", font=("Arial", 12))  # --> creating a component
km_label.grid(row=2, column=2)  # --> run the component
km_label.config(padx=30, pady=10)

# Button
button = tk.Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=1)  # --> run the component
button.config(padx=30, pady=10)





window.mainloop()
