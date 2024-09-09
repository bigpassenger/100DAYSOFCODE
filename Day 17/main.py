from data import question_data
from question_model import Question

def start_game():
    question_bank = []
    for question in question_data:
        answer=question['answer']
        text=question['text']
        object1 = Question(answer,text)
        question_bank.append(object1)

    print(question_bank)


start_game()