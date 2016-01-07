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

def square(lst):
    # Needs only one argument
    return lst[1] ** 2


def cube(lst):
    # Needs only one argument
    return lst[1] ** 3


def power(lst):
    return lst[1] ** lst[2]  # ** = exponent operator


def mod(lst):
    return lst[1] % lst[2]
