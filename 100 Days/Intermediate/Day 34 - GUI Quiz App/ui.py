from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create canvas for question card
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 100,
            width=280,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 13, "italic")
        )
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Create label for score tracker
        self.score_label = Label(
            text=f"Your Score: {self.quiz.score}/10",
            fg="white",
            font=("Arial", 13, "bold"),
            bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0, pady=5)

        # Create buttons
        check_image = PhotoImage(file="images/true.png", width=100, height=99)
        self.true_button = Button(
            image=check_image,
            highlightthickness=0,
            command=self.answer_true
        )
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        cross_image = PhotoImage(file="images/false.png", width=100, height=99)
        self.false_button = Button(
            image=cross_image,
            highlightthickness=0,
            command=self.answer_false
        )
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

