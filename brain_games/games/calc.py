import random

TASK = 'What is the result of the expression?'

def get_correct_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    exp = random.choice('+-*')
    if exp == '+':
        correct_answer = number1 + number2
    elif exp == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return number1, number2, exp, correct_answer

def get_round():
    number1, number2, exp, correct_answer = get_correct_answer()
    question = f'{number1} {exp} {number2}'
    return question, correct_answer
