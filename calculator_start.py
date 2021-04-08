#!/usr/bin/env python

from diverse_logos import calc_logo
print(calc_logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

add(3, 4)
subtract(9, 3)
multiply(3, 3)
divide(9, 3)

operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        }

def calculator():
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    calc_finished = False

    while not calc_finished:
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        print(f"Type 'y' to continue calculation with {answer},")
        print(f"type 'n' to start a new calculation or")
        user_input = input(f"type 'x' to exit: ")
        if user_input == "y":
            num1 = answer
        elif user_input == "n":
            calc_finished = True
            calculator()
        else:
            break

calculator()
