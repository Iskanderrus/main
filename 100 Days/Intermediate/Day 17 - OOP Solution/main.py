from question_model import Question
from data import question_data


data_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    data_bank.append(new_question)
