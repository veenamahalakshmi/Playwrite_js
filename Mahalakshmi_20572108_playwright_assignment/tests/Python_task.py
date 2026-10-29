# Exported from Python_task.ipynb. Run cells individually in VS Code.

# %%
# Day 4 Task 1 Mahalakshmi _20572108

# Store personal details and display each variable's data type.
name = "Mahalakshmi"
age = 0  # Replace with your age.
currently_working = False  # Replace with your current work status.
result = None  # The result is not known yet.
work_experience_years = 0  # Replace with your years of experience.

print("name:", type(name))
print("age:", type(age))
print("currently_working:", type(currently_working))
print("result:", type(result))
print("work_experience_years:", type(work_experience_years))

# %%
# Task 2_Mahalakshmi-20572108

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero."
    return a / b


def main():
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose an operation (1-4): ").strip()
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Please choose a number from 1 to 4.")
        return

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    operations = {
        "1": ("Sum", add),
        "2": ("Difference", subtract),
        "3": ("Product", multiply),
        "4": ("Quotient", divide),
    }
    label, operation = operations[choice]
    print(f"{label}: {operation(first_number, second_number)}")


if __name__ == "__main__":
    main()

# %%
# Assign two numbers to variables and print their sum
a = 10
b = 25
print(a + b)

# Print with standard spacing
print("Hello world")
print("Hello world")

# Try extra spaces around the function name
print( "Hello world" )

# Print the same simple text using single quotes and double quotes
print('Hello world')
print("Hello world")

# Print text that contains an apostrophe
print("It's working")

# Print two short phrases on separate lines using \n
print("First line\nSecond line")

# Add a single-line comment
# This is a single-line comment

# Add a multi-line comment containing your name or employee ID
"""
This is a multi-line comment example
Name: Pramod
Employee ID: 12345
"""

# This prints normally
print("This is a comment demo")

# %%
#Mahalakshmi - 20572108

a = 10
b = 3

# Addition, subtraction, and multiplication
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Exponentiation compared with repeated multiplication
print("10 ** 3 =", 10 ** 3)
print("10 * 10 * 10 =", 10 * 10 * 10)

# Order of operations: multiplication happens before addition
print("2 + 3 * 4 =", 2 + 3 * 4)

# Parentheses change the order
print("(2 + 3) * 4 =", (2 + 3) * 4)

# Division, floor division, and remainder
print("10 / 3 =", 10 / 3)
print("10 // 3 =", 10 // 3)
print("10 % 3 =", 10 % 3)

# An odd number divided by 2 leaves a remainder of 1
print("7 % 2 =", 7 % 2)

# %%
# Day 2 Mahalakshmi_20572108

import os
import platform

print("Name: Mahalakshmi")
print("Operating system:", platform.system())
print("Operating-system version:", platform.version())
print("Python version:", platform.python_version())
print("Current working directory:", os.getcwd())

# %%
# Task 2 - Mahalakshmi_20572108

first_name = "Mahalakshmi"
last_name = "YourLastName"  # Replace with your last name

# Print the first name
print("First name:", first_name)

# Join first and last names with and without a space
print("Without a space:", first_name + last_name)
full_name = first_name + " " + last_name
print("With a space:", full_name)

# Print the full name followed by another word
print("Full name and another word:", full_name + " Python")

# Count characters; the space is included in the full name's length
print("Characters in first name:", len(first_name))
print("Characters in full name, including the space:", len(full_name))

# Access characters by index
print("Character at index 0:", full_name[0])

positive_index = 2
print("Character at index", positive_index, ":", full_name[positive_index])

# Access the last character with negative indexing
print("Last character:", full_name[-1])

# Find and use the final valid positive index
last_valid_index = len(full_name) - 1
print("Last valid index:", last_valid_index)
print("Character at the last valid index:", full_name[last_valid_index])

# Try an index beyond the valid range and display the error
try:
    print(full_name[len(full_name)])
except IndexError as error:
    print("IndexError:", error)

# The character at stop_index is excluded from a slice
start_index = 1
stop_index = 5
print("Name slice:", first_name[start_index:stop_index])

# %%
# Task 3 - Mahalakshmi_20572108

# Check voting age
age = 20

if age >= 18:
    print("Age check:", age, "is eligible to vote")
else:
    print("Age check:", age, "is under 18 and cannot vote")


# Check both an odd and an even number
for number in (7, 8):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# Check the requested grade boundaries
for marks in (59, 60, 89, 90, 100):
    if marks >= 90:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    else:
        grade = "C"

    print("Marks:", marks, "Grade:", grade)


# A person must be at least 18 and have an ID to vote
def check_voting_eligibility(age, has_id):
    if age >= 18:
        if has_id:
            print("Age", age, "has_id =", has_id, ": eligible to vote")
        else:
            print("Age", age, "has_id =", has_id, ": rejected - ID required")
    else:
        print("Age", age, "has_id =", has_id, ": rejected - under 18")


# Test ages 16 and 20 with both ID values
check_voting_eligibility(16, True)
check_voting_eligibility(16, False)
check_voting_eligibility(20, True)
check_voting_eligibility(20, False)

# %%
# Mahalakshmi - 20572108_Task1- Day 3

# Task 1 - Check Python's case sensitivity
print("True:", True)
print("False:", False)

# Python recognizes the capitalized boolean literals, not lowercase names.
try:
    print(true)
except NameError:
    print("true (lowercase) is not recognized as a boolean literal")

try:
    print(false)
except NameError:
    print("false (lowercase) is not recognized as a boolean literal")


# Ask for the person's age and whether they have an ID.
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").strip().lower() == "yes"

# Entry requires both conditions: age 18 or older and a valid ID.
if age >= 18 and has_id:
    print("Entry allowed.")
elif age >= 18 and not has_id:
    print("You are old enough, but please bring your ID to enter.")
else:
    print("Entry not allowed: you must be at least 18 years old.")

# %%
# Task 2 - Loops and indentation

# MAHALAKSHMI - 20572108

# Use four spaces for each indentation level in a conditional.
number = 7
if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print("The number is zero")


# Display the multiplication table of 5.
table_number = 5
for multiplier in range(1, 11):
    print(table_number, "x", multiplier, "=", table_number * multiplier)


# Keep asking until the entered password matches the sample password.
sample_password = "python123"
entered_password = ""
while entered_password != sample_password:
    entered_password = input("Enter the password: ")
    if entered_password != sample_password:
        print("Incorrect password. Try again.")
print("Password accepted.")


# Print prime numbers from 1 to 25 (1 is not a prime number).
for candidate in range(2, 26):
    is_prime = True
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(candidate)


# Use a nested loop to print a simple right-triangle pattern.
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()

# %%
# Mahalakshmi - 20572108

# 1) Range basics: loop over range(1, 8)
# Python stops before the end value, so 8 is excluded.
for num in range(1, 8):
    print(num)

print("----")

# 2) Include the endpoint: print numbers 1 through 8 using range()
for num in range(1, 9):
    print(num)

print("----")

# 3) While loop: start at 1 and print values through 5
i = 1
while i <= 5:
    print(i)
    i += 1  # increment inside the loop

print("----")

# 4) Missing increment: what happens if you omit i += 1?
# The loop would keep printing 1 forever because i never changes.
# Example:
# i = 1
# while i <= 5:
#     print(i)
#     # i += 1  # missing
# This would become an infinite loop.

# 5) Positive-number input: keep asking until a positive number is entered
while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        print("You entered:", num)
        break
    else:
        print("That number is not positive. Try again.")

print("----")

# 6) False condition: a while loop with while False
# The body never runs because the condition is already false.
while False:
    print("This will never run")

print("----")

# 7) Skip a value: print 1 to 6 while skipping 3
for num in range(1, 7):
    if num == 3:
        continue
    print(num)

# %%
# Mahalakshmi - 20572108

# Compare loop controls: break vs continue
print("break example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\ncontinue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Nested loops: print every pair of values
print("\nNested loops:")
for i in range(1, 5):
    for j in range(1, 5):
        print(f"({i}, {j})", end=" ")
    print()

# Trace nested loops: order of execution
# Outer loop i = 1,2,3,4
# Inner loop j = 1,2,3,4 for each i
# Order:
# (1,1), (1,2), (1,3), (1,4),
# (2,1), (2,2), (2,3), (2,4),
# (3,1), (3,2), (3,3), (3,4),
# (4,1), (4,2), (4,3), (4,4)

# List of operating systems
os_list = ["Windows", "Linux", "macOS"]

# List and indexes
print("\nList with indexes:")
for index, value in enumerate(os_list):
    print(index, value)

# Append to a list
os_list.append("Ubuntu")
print("\nAfter append:", os_list)

# Remove from a list
os_list.remove("Linux")
print("After remove:", os_list)

# Update a list item
os_list[1] = "Fedora"
print("After update:", os_list)

# %%

# mahalakshmi-20572108


# Invalid index: try accessing an index beyond the list length and identify the error
numbers = [10, 20, 30]
print("List:", numbers)

try:
    print(numbers[5])   # invalid index
except IndexError as error:
    print("IndexError:", error)

# Assignment vs comparison:
# Use '=' to assign a value, then '==' to test whether a value matches it.
x = 10
print("x =", x)
print("x == 10:", x == 10)

# Create a tuple: store several peripheral names in a tuple and access one by index
peripherals = ("keyboard", "mouse", "monitor", "speaker")
print("Tuple item at index 2:", peripherals[2])

# Tuple immutability: try changing one tuple item and observe the result
try:
    peripherals[1] = "printer"
except TypeError as error:
    print("TypeError:", error)

# List versus tuple: create equivalent list and tuple values
list_peripherals = ["keyboard", "mouse", "monitor"]
tuple_peripherals = ("keyboard", "mouse", "monitor")

print("List before update:", list_peripherals)
list_peripherals[1] = "printer"   # allowed
print("List after update:", list_peripherals)

print("Tuple before update:", tuple_peripherals)
# tuple_peripherals[1] = "printer"   # this would raise TypeError because tuples are immutable

# Do-while style behavior:
# Python has no built-in do-while loop, so use while True and break
while True:
    name = input("Enter your name: ")
    if name.strip() != "":
        print("Hello,", name)
        break
    print("Name cannot be empty. Please try again.")

# %%
# Task 3 - Mahalakshmi_20572108

import math

square_root = math.sqrt(81)
rounded_up = math.ceil(6.2)
rounded_down = math.floor(6.8)

print("Square root of 81:", square_root)
print("6.2 rounded up:", rounded_up)
print("6.8 rounded down:", rounded_down)
