"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    question = raw_input()
    token = question.split(" ")
    token[1] = int(token[1])
    token[2] = int(token[2])
    if token[0] == "q":
        break
    elif token[0] == "+":
        print add(token[1], token[2])
    elif token[0] == "-":
        print subtract(token[1], token[2])
    elif token[0] == "*":
        print multiply(token[1], token[2])
    elif token[0] == "/":
        print divide(token[1], token[2])
    elif token[0] == "square":
        print square(token[1])
    elif token[0] == "cube":
        print cube(token[1])
    elif token[0] == "pow":
        print power(token[1], token[2])
    elif token[0] == "mod":
        print mod(token[1], token[2])
    else:
        question = raw_input()
