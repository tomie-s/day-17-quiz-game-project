class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        new_question = self.q_list[self.q_number]
        text = new_question.text
        self.q_number += 1
        user_answer = input(f"Q. {self.q_number}: {text} (True/False)?: ")
        correct_answer = new_question.answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer == c_answer:
            self.score += 1
            print("You are correct!")
        else:
            print("Sorry, you got it wrong.")
        print(f"The correct answer was: {c_answer}.")
        print(f"You current score is {self.score}/{self.q_number}")
        print("\n")
