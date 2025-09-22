"""

    get number_of_gifts
    get number_of_students
    gifts_per_student = number_of_gifts // number_of_students
    remaining_gifts = number_of_gifts % number_of_students
    display "Each student gets ", gifts_per_student, " gifts."
    display "Remaining gifts: ", remaining_gifts

number_of_gifts = int(input("Enter total number of gifts: "))
number_of_students = int(input("Enter total number of students: "))
gifts_per_student = number_of_gifts // number_of_students
remaining_gifts = number_of_gifts % number_of_students
print("Each student gets ", gifts_per_student, " gifts.")
print("Remaining gifts: ", remaining_gifts)

"""
"""
get the item price
ask whether GST applies
apply GST if selected (let's assume GST = 9%)
print final price in currency format
print(f"Final price: ${price:.2f}")

GST = 0.9
item_price = float(input("Enter item price: "))
gst_choice = input("Does it have GST? (y/n): ")
if gst_choice == "y":
  final_price = item_price * 0.9
else:
    final_price = item_price
print("Final price: ", final_price)


#Method 1: Using while loop
number = int(input("Enter a number: "))
i = 1
while i <= number:
    print(i, end=" ")
    i += 1

#Method 2: Using for loop
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    print(i, end=" ")


import random
SECRET = random.randint(1,10)
guess_count = 0
print("Guess the secret number (between 1 and 10)")
while True:
    guess = int(input("Guess a number: "))
    guess_count += 1
    if guess < SECRET:
        print("Higher")
    elif guess > SECRET:
        print("Lower")
        print(f"You got it in {guess_count} guesses!")
        break




name = input("Enter your name: ")
while name == "":
    print("Name cannot be blank. Please try again.")
    name = input("Enter your name: ")
salary = float(input("Enter your salary: "))
while salary < 0:
    print("Salary cannot be below zero. Please try again.")
    salary = float(input("Enter your salary: "))
print("Name:", name.upper())
print(f"Salary: ${salary:.2f}")


TOTAL_AGE = 0
count = int(input("How many people are in the room? "))
for i in range(1, count + 1):
    age = int(input(f"Enter age of person {i}: "))
    TOTAL_AGE += age
average_age = TOTAL_AGE / count if count > 0 else 0

print(f"Total of ages: {TOTAL_AGE}")
print(f"Average age: {average_age:.2f}")



TOTAL_AGE = 0
COUNT = 0
AGE = 0
while age != -1:
    age = int(input("Enter age (-1 to stop): "))
    TOTAL_AGE += age
    COUNT += 1
average_age = TOTAL_AGE / COUNT

print(f"Total of ages: {TOTAL_AGE}")
print(f"Average age: {average_age:.2f}")




for i in range (1, 4):
    for j in range (2, 10,3):
        print(i,"-",j+i )
        """

