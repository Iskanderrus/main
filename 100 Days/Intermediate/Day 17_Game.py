question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.",
     "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.",
     "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a "
             "football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with "
                "your car, you are free to take it home to eat.",
        "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of "
             "Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.",
     "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.",
     "answer": "True"},
    {"text": "No piece of square dry paper can be folded in "
             "half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.",
     "answer": "True"}
]


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def make_question(self):
        return self.text

    def check_answer(self, user_answer):
        if self.answer.lower() == user_answer.lower():
            print("This is correct answer!")
            return True
        else:
            print("This is wrong answer")
            return False


def game():
    score = 0
    counter = 0
    while counter < len(question_data):
        for question in question_data:
            counter += 1
            new_question = Question(question["text"], question["answer"])
            users_answer = input(f"Q. {counter}: {new_question.make_question()} "
                                 f"True or False: ")
            if new_question.check_answer(users_answer):
                score += 1
                print(f"Your score is {score} of {len(question_data)}.\n")
            else:
                print(f"No points to score. Your score remains {score} of "
                      f"{len(question_data)}.\n")


if __name__ == '__main__':
    game()
