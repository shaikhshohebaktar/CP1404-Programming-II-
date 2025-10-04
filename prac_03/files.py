"""
CP1404 - Practical Files Exercises
"""

# Part1 Ask for name and write to file
name = input("Enter your name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)

# Part2: Read name from file and print greeting
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print(f"Hi {name}!")

# Part3 Sum first two numbers in numbers.txt
with open("numbers.txt", "w") as out_file:
    print("17", file=out_file)
    print("42", file=out_file)
    print("400", file=out_file)

with open("numbers.txt", "r") as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
print(num1 + num2)

# Part4 Sum all numbers in file
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
print(total)
