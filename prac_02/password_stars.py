MINIMUM_LENGTH = 10

password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Invalid password minimum length {MINIMUM_LENGTH} characters long")
    password = input("Password: ")
print("*" * len(password))
