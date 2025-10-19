def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name} (Y/N)").strip().lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    print()

    for email, name in email_to_name.items():
        print(f"{name} {email}")


def get_name_from_email(email):
    name_part = email.split("@")[0]
    parts = name_part.split('.')
    name = " ".join(parts).title()
    return name


main()
