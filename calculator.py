"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term

def division(numerator, denumerator):
    if denumerator == 0:
        print("Can divide by zero")
    else:
        return numerator/denumerator
