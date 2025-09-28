"""Module docstring"""

MINIMUM_LENGTH = 10


def main():
    """Function docstring"""
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Invalid password minimum length {MINIMUM_LENGTH} characters long")
        password = input("Password: ")
    return password


def print_stars(password):
    print("*" * len(password))


main()
