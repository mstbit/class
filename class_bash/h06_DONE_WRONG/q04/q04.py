#!/usr/bin/python3
num = input("Please enter a number: ")
num = int(num)
data_type = type(num)

# print(data_type)		### the type of data_type is integer

data_type = str(data_type)
# print((type(data_type))	### the type of data_type is now string

if data_type == "<class 'int'>":

    print("You have entered an integer.")
else:
    print("shoot")
