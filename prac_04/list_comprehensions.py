"""
CP1404 Practical
List comprehensions
"""

def main():
    """Run examples of list comprehensions."""
    names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
    full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

    print(get_first_initials(names))
    print(get_full_initials(full_names))
    print(get_a_names(names))
    print(" ".join(sorted(names)))
    print(get_lowercase_full_names(full_names))

    almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
    numbers = convert_to_numbers(almost_numbers)
    print(numbers)
    print(get_numbers_over_nine(numbers))
    print(get_long_last_names(full_names))


def get_first_initials(names):
    """Return a list of first initials from the given list of names."""
    return [name[0] for name in names]


def get_full_initials(full_names):
    """Return a list of initials from the given list of full names."""
    return [name.split()[0][0] + name.split()[1][0] for name in full_names]


def get_a_names(names):
    """Return a list of names that start with 'A'."""
    return [name for name in names if name.startswith('A')]


def get_lowercase_full_names(full_names):
    """Return all full names in lowercase format."""
    return [name.lower() for name in full_names]


def convert_to_numbers(almost_numbers):
    """Convert a list of numeric strings to integers."""
    return [int(num) for num in almost_numbers]


def get_numbers_over_nine(numbers):
    """Return numbers greater than 9 from the given list."""
    return [num for num in numbers if num > 9]


def get_long_last_names(full_names):
    """Return a string of last names for full names longer than 11 characters."""
    return ", ".join([name.split()[1] for name in full_names if len(name) > 11])


if __name__ == "__main__":
    main()
