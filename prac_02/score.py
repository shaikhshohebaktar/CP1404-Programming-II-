"""Score program with functions."""

import random


def main():
    score = float(input("Enter score: "))
    print(get_result(score))
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(get_result(random_score))
def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
