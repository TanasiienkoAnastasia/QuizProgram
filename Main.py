quiz = {
    "question1": {
        "question": "What is the capital of the France?",
        "answer": "Paris"
    },"question2": {
        "question": "What is the capital of the Germany?",
        "answer": "Berlin"
    },"question3": {
        "question": "What is the capital of the Italy?",
        "answer": "Rome"
    },"question4": {
        "question": "What is the capital of the Spain?",
        "answer": "Madrid"
    },"question5": {
        "question": "What is the capital of the Portugal?",
        "answer": "Lisbon"
    },"question6": {
        "question": "What is the capital of the Switzerland?",
        "answer": "Bern"
    },"question7": {
        "question": "What is the capital of the Austria?",
        "answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score + 1
        print("Your score is: " + str(score))

    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))