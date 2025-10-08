"""
CP1404 Practical
List exercises
"""

def main():
    numbers = get_numbers(5)
    display_number_stats(numbers)
    check_username()


def get_numbers(count):
    """Prompt the user for `count` numbers and return them as a list."""
    numbers = []
    for i in range(count):
        number = int(input(f"Number {i + 1}: "))
        numbers.append(number)
    return numbers


def display_number_stats(numbers):
    """Display statistics about the list of numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average:.1f}")


def check_username():
    """Check if a user is authorised to access the system."""
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
    ]
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
