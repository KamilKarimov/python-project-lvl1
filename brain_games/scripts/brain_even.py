#!/usr/bin/python3
from random import randint
import prompt


def is_even(number):
    return number % 2 == 0


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = randint(1, 100)
        if is_even(number):
            correct_answer = "yes"
        else:
            correct_answer = "no"
        counter = 0
        while counter != 3:
            question = print(f'Question: {number}')
            user_answer = prompt.string('Your answer: ')
            if user_answer == correct_answer:
                print('Correct!')
                counter += 1
            else:
                print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}. Let's try again, {name}!")
                break
    print(f'Congratulations, {name}!')



if __name__ == '__main__':
    main()
