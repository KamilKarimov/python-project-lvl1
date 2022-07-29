import random

TASK = 'What number is missing in the progression?'


def get_round():
    num = random.randint(1, 10)
    progression = [(x * num) for x in range(1, 10)]
    random_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(
        '..' if num == correct_answer else str(num) for num in progression
    )
    return question, correct_answer
