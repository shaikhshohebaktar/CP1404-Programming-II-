"""
CP1404 Practical Emails
"""

def main():
    """Store users' emails and names in a dictionary."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y"):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a possible name from the email address."""
    username = email.split('@')[0]
    parts = username.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()
