#!/usr/bin/python3

# Prompt the user to input an integer
num = input("Please input an integer: ")

# Convert input to integer
num = int(num)

# Check the type of the input object
input_type = type(num)

# Output the result of type checking
print("The type of the input is:", input_type)