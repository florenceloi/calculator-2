# written by florenceloi and celiawaggoner

"""
calculator-reduce.py

Using our calculator.py file from Exercise02, rewrite using reduce function.
"""

from arithmetic import *


# Your code goes here
while True:
    question = raw_input("> ")
    token = question.split()
    try:
        token[1:] = map(float, token[1:])
    except ValueError:
        print "That's not a valid command. Try again!"
        break

    operators = ["+", "-", "*", "/", "pow", "mod", "square", "cube"]

    if len(token) == 1:
        if token[0] == "q":
            break
    elif len(token) > 1:
        if token[0] in operators:
            if token[0] in operators[:6]: 
                if len(token) >= 3:
                    if token[0] == "+":
                        print add(token)
                    elif token[0] == "-":
                        print subtract(token)
                    elif token[0] == "*":
                        print multiply(token)
                    elif token[0] == "/":
                        print divide(token)
                    elif token[0] == "pow":
                        print power(token)
                    elif token[0] == "mod":
                        print mod(token)
                else:
                    print "Not enough numbers"
            if token[0] in operators[6:]:
                if token[0] == "square":
                    print square(token)
                elif token[0] == "cube":
                    print cube(token)
        else:
            print "Operator not valid."
    else:
        print "That's not a valid command. Try again!"

