"""
CP1404 - Practical Password checker
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
REQUIRES_SPECIAL_CHARS = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("    1 or more uppercase characters")
    print("    1 or more lowercase characters")
    print("    1 or more numbers")
    if REQUIRES_SPECIAL_CHARS:
        print(f"    and 1 or more special characters:  {SPECIAL_CHARACTERS}")

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)} character password is valid: {password}")


def is_valid_password(password: str) -> bool:
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for ch in password:
        if ch.islower():
            count_lower += 1
        elif ch.isupper():
            count_upper += 1
        elif ch.isdigit():
            count_digit += 1
        elif ch in SPECIAL_CHARACTERS:
            count_special += 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if REQUIRES_SPECIAL_CHARS and count_special == 0:
        return False

    return True


main()
