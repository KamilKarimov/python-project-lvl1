#!/usr/bin/python3
import random

TASK = 'What is the result of the expression?'

 
def get_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    exp = random.choice('+-*')
    question = f'{number1} {exp} {number2}'
    correct_answer = eval(f'{number1} {exp} {number2}')
    return question, correct_answer