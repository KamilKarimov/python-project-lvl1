#!/usr/bin/python3
import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_round():
    number = random.randint(1, 100)
    question = number
    if is_even(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
