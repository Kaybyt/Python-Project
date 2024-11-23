import random
import threading
import time


## QUESTION AND ANSWER HANDLING
# 1. Display multiple-choice questions to the user.

questions = [{"question": "Who's the president of Nigeria?",
        "options": ["A. Buhari", "B. Atiku", "C. Tinubu", "D. Shettima"],
        "answer": "C"}, 
        {"question": "How many states are there in Nigeria?",
        "options": ["A. 25", "B. 36", "C. 39", "D. 40"],
        "answer": "B"},
        {"question": "Where's GoMyCode Abuja located?", "options": ["A. Jabi", "B. Maitama", "C. Wuse2", "D. Gwarimpa"],
         "answer": "C"}]

# 2. Capture and validate user inputs.
def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Choose the correct answer (A, B, C, D): ").upper()
    return answer

def check_answer(question, user_answer):
    return user_answer == question["answer"]

# 3. Provide immediate feedback on the correctness of answers.

def quiz_game(questions):
    score = 0
    for question in questions:
        user_answer = ask_question(question)
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")
    print(f"Your final score is {score}/{len(questions)}")

## Display the questions

if __name__ == "__main__":
    quiz_game(questions)

## Implement a timer for each question to add a time-based challenge.

def ask_question_with_timer(question, time_limit):
    print(question["question"])
    for option in question["options"]:
        print(option)

    timer = threading.Timer(time_limit, print, ["Time's up!"])
    timer.start()
    answer = input("Choose the correct answer (A, B, C, D): ").upper()
    timer.cancel()
    return answer

## Randomly shuffle the order of questions for each game session to enhance replayability.
random.shuffle(questions)
quiz_game(questions)


## Store and display high scores from previous sessions.

def save_high_score(score, filename="high_scores.txt"):
    with open(filename, "a") as file:
        file.write(f"{score}\n")

def display_high_scores(filename="high_scores.txt"):
    with open(filename, "r") as file:
        scores = file.readlines()
    scores = [int(score.strip()) for score in scores]
    scores.sort(reverse=True)
    print("High Scores:")
    for score in scores[:5]:
        print(score)

