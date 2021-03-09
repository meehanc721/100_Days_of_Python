#! python3
# Calculator.py - self explanatory
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    number = float(input("First Number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue == True:
        op_symbol = input("Pick operation: ")
        next_number = float(input("Next number: "))

        calculation_function = operations[op_symbol]
        answer = calculation_function(number, next_number)

        print(f"{number} {op_symbol} {next_number} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
            number = answer
        else:
            should_continue = False
            calculator()


calculator()
