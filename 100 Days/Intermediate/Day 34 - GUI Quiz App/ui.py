from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        # Create window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        # Create canvas for question card
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 100, text="Title", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        # Create label for score tracker
        self.score_label = Label(text="Your Score: ", fg="white", font=("Arial", 13, "bold"), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, padx=20, pady=5)
        # Create buttons
        check_image = PhotoImage(file="images/true.png", width=100, height=99)
        self.true_button = Button(image=check_image, highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        cross_image = PhotoImage(file="images/false.png", width=100, height=99)
        self.false_button = Button(image=cross_image, highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()
