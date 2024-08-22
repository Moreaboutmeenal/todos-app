import json
import random
with open("questions.json",'r') as file:
    content = file.read()
score = 0
data = json.loads(content)
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    user_choice = int(input("Enter your answer: \n"))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score = score+1
for index, question in enumerate(data):
    message = f"{index+1}. Your answer: {question['user_choice']},"\
              f"Correct answer: {question['correct_answer']}"
    print(message)

print(data)
print("Your Score is:", score,"/", len(data))
print("Your score is good")

low_num = int(input("Enter the lower bound"))
up_num = int(input("Enter the upper bound"))
rand = random.randrange(low_num,up_num+1)
print(rand)