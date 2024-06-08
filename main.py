from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    text = item['question']
    answer = item['correct_answer']

    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz_game = QuizBrain(question_bank)

while quiz_game.still_has_questions():
    quiz_game.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz_game.score}/{quiz_game.q_number}")
