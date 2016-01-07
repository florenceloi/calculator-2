"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    question = raw_input("> ")
    token = question.split()
    # try:
    token[1:] = map(int, token[1:])
    # except IndexError:
    #     pass
    # try:
    #     token[2] = int(token[2])
    # except IndexError:
    #     pass
    # try:
    #     token[3] = int(token[3])
    # except IndexError:
    #     pass
    if len(token) == 1:
        if token[0] == "q":
            break
    elif len(token) == 2:
        if token[0] == "square":
            print square(token[1])
        elif token[0] == "cube":
            print cube(token[1])
    elif len(token) == 3:
        if token[0] == "pow":
            print power(token[1], token[2])
        elif token[0] == "mod":
            print mod(token[1], token[2])
    elif len(token) > 3:
        if token[0] == "+":
            print add(token)
        elif token[0] == "-":
            print subtract(token)
        elif token[0] == "*":
            print multiply(token)
        elif token[0] == "/":
            print divide(token)
    else:
        question = raw_input()
