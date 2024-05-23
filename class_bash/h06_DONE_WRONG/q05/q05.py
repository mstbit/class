#!/usr/bin/python
# Get user input for age
age_input = input("Enter your age: ")

# Check if input is a numeric value
if age_input.isdigit():
    age = int(age_input)
    # Check eligibility based on age
    if age < 16:
        print("You are too young for a learner's permit.")
    elif age >= 16 and age < 18:
        print("You are eligible for a learner's permit.")
    else:
        print("You do not need a learner's license.")
else:
    print("Invalid input: input must be a numeric value.")
