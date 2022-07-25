#!/usr/bin/python3
import random

TASK = 'What number is missing in the progression?'


def get_round():
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
        question = ' '.join(
        '..' if num == correct_answer else str(num) for num in progression)
    return question, correct_answer
