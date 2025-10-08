"""
CP1404 Practical
subject reader
"""
FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects()
    display_subjects(subjects)


def load_subjects():
    """Load subject data into a list of lists."""
    subjects = []
    with open(FILENAME) as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    for subject in subjects:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")


if __name__ == "__main__":
    main()
