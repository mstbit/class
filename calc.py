def add_two(num1, num2):
    return num1 + num2


def add_multiple(*args):
    total = 0
    for num in args:
        total = total + num
    return total


total = add_multiple(1, 2, 3, 4, 5)
print(total)

# add elements of a list together using a for loop


def add_list_for_loop(lst):
    total = 0
    for num in lst:
        total = total + num
    return total


lst = [1, 2, 3, 4, 5]
total = add_list_for_loop(lst)
print(total)


# add elements of a list together using the list total function
def add_list_total(l):
    # total = total(l)
    # return total
    return sum(l)

# print(lst)
total = add_list_total(lst)
print(total)

# mean of data


# median of data


# mode of data


# variance


# standard deviation
