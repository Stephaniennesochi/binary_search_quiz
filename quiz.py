quiz = {
    "question1": {
        "question": {"What is the capital of France?"},
        "answer": "Paris"
    },
    "question2": {
        "question": {"What is the capital of Germany?"},
        "answer": "Berlin"
    },
    "question3": {
        "question": {"What is the capital of Italy?"},
        "answer": "Rome"
    },
    "question4": {
        "question": {"What is the capital of Spain?"},
        "answer": "Madrid"
    },
    "question5": {
        "question": {"What is the capital of Portugal?"},
        "answer": "Lisbon"
    },
    "question6": {
        "question": {"What is the capital of Switzerland?"},
        "answer": "Bern"
    },
    "question7": {
        "question": {"What is the capital of Austrial?"},
        "answer": "Vienna"
    },
}
score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer?")
    
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1
        print("Your score is " + str(score))