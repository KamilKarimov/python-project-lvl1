#!/usr/bin/python3
import prompt
import random


def calc(number1, number2, exp):
    correct_answer = f'{number1} {exp} {number2}'


def calc_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    counter = 0
    while counter != 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        exp = random.choice('+', '-', '*')
        print(f'Question: {number1} {exp} {number2}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
