"""
CP1404 Practical ProgrammingLanguage class
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic=False):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return a nicely formatted string representation."""
        reflection_status = "Yes" if self.reflection else "No"
        pointer_status = "Yes" if self.pointer_arithmetic else "No"
        return (f"{self.name}, {self.typing} Typing, Reflection={reflection_status}, "
                f"Pointer Arithmetic={pointer_status}, First appeared in {self.year}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing.lower() == "dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983, True)

    languages = [ruby, python, visual_basic, c_plus_plus]
    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
