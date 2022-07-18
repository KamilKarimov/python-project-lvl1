#!/usr/bin/python3
import prompt
import random


def gcd_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    for _ in range(3):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        correct_answer = number1
        while correct_answer > 0:
            if number1 % correct_answer == 0 and number2 % correct_answer == 0:
                break
            correct_answer -=1
        print(f'Question: {number1} {number2}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(correct_answer):
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        if counter == 3:
            print(f'Congratulations, {name}!')
   