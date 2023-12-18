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
