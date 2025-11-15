"""CP1404 Practical More Guitars!"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Read guitars file, display, add new, and save back."""
    guitars = load_guitars(FILENAME)
    guitars.sort()

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    print()
    add_new_guitars(guitars)
    save_guitars(FILENAME, guitars)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}.")


def load_guitars(filename):
    """Load guitars from file into a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def add_new_guitars(guitars):
    """Allow user to add new guitars."""
    print("Enter your new guitars (leave name blank to finish):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save list of guitars back to file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
