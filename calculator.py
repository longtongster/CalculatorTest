"""
Calculator library containing basic math operations.

Code taken from real python website
"""

def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    print("sacha")
    return first_term * second_term


def division(numerator, denumerator):
    if denumerator == 0:
        print("Can divide by zero")
    else:
        return numerator/denumerator
