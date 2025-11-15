"""
CP1404 Practical
Reads  programming language
"""

from programming_language import ProgrammingLanguage


def main():
    """Read programming language data from file and display it."""
    languages = []
    with open('languages.csv', 'r', encoding='utf-8') as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            typing = parts[1]
            reflection = parts[2] == "Yes"
            year = int(parts[3])
            pointer_arithmetic = parts[4] == "Yes"
            languages.append(ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic))

    print("Programming Languages loaded:\n")
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()
