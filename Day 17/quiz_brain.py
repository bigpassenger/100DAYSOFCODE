class QuizBrain:

    def __init__(self,questionlist):
        self.question_number = 0
        self.question_list = questionlist
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def check_answer(self,user_answer,answer):
        if user_answer.lower() == answer.lower():
            print('You got it')
            self.score += 1
        else:
            print("That's Wrong")


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        print(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
        user_answer = input()
        self.check_answer(user_answer,current_question.answer)

        return self.score
