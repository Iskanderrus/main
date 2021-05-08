import data


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


data_bank = []
counter = 0
while counter < len(data.question_data):
    for question in data.question_data:
        new_text = data.question_data[counter]["text"]
        new_answer = data.question_data[counter]["answer"]
        new_question = Question(new_text, new_answer)
        data_bank.append(new_question)
        counter += 1

print(data_bank)
