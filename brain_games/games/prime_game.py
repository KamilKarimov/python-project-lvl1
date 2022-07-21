#!/usr/bin/python3
import prompt
import random


def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True


def prime_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    for _ in range(3):
        number = random.randint(2, 100)
        if is_prime(number):
            correct_answer = "yes"
        else:
            correct_answer = "no"
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        if counter == 3:
            print(f'Congratulations, {name}!')
