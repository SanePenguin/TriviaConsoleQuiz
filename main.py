from data import question_data
from question_model import Question

question_bank = []
for q in question_data:
    question_bank.append(Question(q_text=q["text"], q_answer=q["answer"]))

print(question_bank[0].text)