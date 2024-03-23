class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False
    
    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong! ")
            print(f"The correct answer was: {correct_answer.lower()}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = current_question.text
        question_answer  = current_question.answer
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        self.check_answer(user_answer=user_answer, correct_answer=question_answer)
        
    
        
        
    
        
        
    
        
    