import data
import question_model
import quiz_brain

question_bank = []

for item in data.question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    question = question_model.Question(question_text, question_answer)
    question_bank.append(question)

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")