#!/usr/bin/python3
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    return name


def get_result():
    if user_answer == str(correct_answer):
        print('Correct!')
        counter += 1
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return
