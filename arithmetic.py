def add(lst):
    total = 0
    for item in lst[1:]:
        total += item
    return total


def subtract(lst):
    total = lst[1]
    for item in lst[2:]:
        total -= item
    return total


def multiply(lst):
    total = lst[1]
    for item in lst[2:]:
        total *= item
    return total


def divide(lst):
    # Need to turn at least argument to float for division to
    # not be integer division
    total = lst[1]
    for item in lst[2:]:
        total /= item
    return total

def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
