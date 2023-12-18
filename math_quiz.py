def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

def generate_quiz_question():

    import random
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    question = f"{x} {operator} {y}"
    answer = eval(question) 
    return question, answer

def play_quiz():
    score = 0
    num_questions = 5  
    for _ in range(num_questions):
        question, answer = generate_quiz_question()
        user_answer = input(f"What is the answer to {question}? ")
        try:
            user_answer = float(user_answer)
            if user_answer == answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {answer}\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    print(f"Quiz completed! Your score is {score}/{num_questions}")

if __name__ == "__main__":
    play_quiz()

