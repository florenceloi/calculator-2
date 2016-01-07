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
    token[1:] = map(float, token[1:])

    if len(token) == 1:
        if token[0] == "q":
            break

    operators = ["+", "-", "*", "/", "square", "cube", "pow", "mod"]

    if token[0] in operators:
        if token[0] == "+":
            print add(token)
        elif token[0] == "-":
            print subtract(token)
        elif token[0] == "*":
            print multiply(token)
        elif token[0] == "/":
            print divide(token)
        elif token[0] == "square":
            print square(token)
        elif token[0] == "cube":
            print cube(token)
        elif token[0] == "pow":
            print power(token)
        elif token[0] == "mod":
            print mod(token)
    else:
        print "Operator not valid."



