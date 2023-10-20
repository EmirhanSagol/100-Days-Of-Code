class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.quiz_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.quiz_list):
            return True
        print("Game is end")
        print(f"Your score is: {self.score}")
        return False

    def next_question(self):
        current_question = self.quiz_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Correct answer: {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}")
        print("\n")
