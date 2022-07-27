#!/usr/bin/python3
import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True


def get_round():
    number = random.randint(2, 100)
    question = number
    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
