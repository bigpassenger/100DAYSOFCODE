from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def start_game():
    wall = """
        '
        '                                   
        '                                   
        """
    question_bank = []
    for question in question_data:
        answer=question['answer']
        text=question['text']
        object1 = Question(answer,text)
        question_bank.append(object1)
    
    quiz = QuizBrain(question_bank)
    
    while True:
        if quiz.still_has_question():
            print('your current score is: ',quiz.next_question())
        else:
            print()
            print()
            print('"-------------------------------------"')
            print(f'Your Final Score: {quiz.score} ')
            print('"-------------------------------------"')
            break


start_game()