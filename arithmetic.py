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
    squares = []
    for item in lst[1:]:
        squares.append(item ** 2)
    return squares


def cube(lst):
    # Needs only one argument
    cubes = []
    for item in lst[1:]:
        cubes.append(item ** 3)
    return cubes


def power(lst):
    total = lst[1]
    for item in lst[2:]:
        total = total ** item
    return total  # ** = exponent operator


def mod(lst):
    quotient = lst[1]
    for item in lst[2:-1]:
        quotient = quotient / item
    return quotient % lst[-1] 
    
