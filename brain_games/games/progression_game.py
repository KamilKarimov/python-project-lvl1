#!/usr/bin/python3
import prompt
import random


def progression_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    counter = 0
    for _ in range(3):
        num = random.randint(1, 10)
        progression = [(x * num) for x in range(1, 10)]
        random_index = random.randint(0, len(progression) - 1)
        progression[random_index] = '..'
        index = progression.index('..')
        if index != 0:
            correct_answer = progression[index - 1] + num
        else:
            correct_answer = progression[index + 1] - num
        print('Question: ', end='')
        print(*progression, sep=' ')
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
