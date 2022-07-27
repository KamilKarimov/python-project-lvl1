#!/usr/bin/python3
import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_round():
    num = random.randint(1, 100)
    question = num
    if is_even(num):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
