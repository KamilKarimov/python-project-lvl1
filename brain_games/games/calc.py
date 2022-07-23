#!/usr/bin/python3
import prompt
import random
from brain_games.logic import welcome_user
from brain_games.logic import get_result

 
def calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    counter = 0
    while counter != 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        exp = random.choice('+-*')
        correct_answer = eval(f'{number1} {exp} {number2}')
        print(f'Question: {number1} {exp} {number2}')
        user_answer = prompt.string('Your answer: ')
        get_result(user_answer, correct_answer, name)
    print(f'Congratulations, {name}!')
