from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

#start game
while quiz.still_has_questions():
    quiz.next_question()

score = quiz.getScore()
print("You've completed the quiz!")
print(f"Your final score is: {score[0]}/{score[1]}.")