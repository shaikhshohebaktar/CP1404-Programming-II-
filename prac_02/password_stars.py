""" password check program with function """


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("enter your password: ")
    while len(password) < 4:
        print("password must be at least 4 characters")
        password = input("enter your password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
