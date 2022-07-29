import random

TASK = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(number1, number2):
    correct_answer = number1
    while correct_answer > 0:
        if number1 % correct_answer == 0 and number2 % correct_answer == 0:
            break
        correct_answer -= 1
    return correct_answer


def get_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    correct_answer = calculate_gcd(number1, number2)
    return question, correct_answer
