"""
Basic calculator for demonstrating Git merge conflicts.
Shows how parallel development can lead to conflicts when
multiple developers modify the same file.
"""


def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def divide_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: cannot divide by zero")


def multiply_numbers(num1, num2):
    return num1 * num2


if __name__ == "__main__":
    print("This is a simple calculator.")
    print(f"Addition: 5 + 3 = {add_numbers(5, 3)}")
    print(f"Subtraction: 10 - 4 = {subtract_numbers(10, 4)}")
    print(f"Divide: 10 / 2 = {divide_numbers(10, 2)}")
    print(f"Divide: 10 / 0 = {divide_numbers(10, 0)}")
    print(f"Multiplication: 6 * 3 = {multiply_numbers(6, 3)}")
