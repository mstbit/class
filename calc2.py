print('Warming Up')

### Two Parameters
def add_two(num1, num2):
    return num1 + num2

print('add two: ', add_two(5, 10))

### Multiple Parameters
def add_multiple(*args):
    total = 0
    for num in args:
        total = total + num
    return total 

total = add_multiple(1, 2, 3, 4, 5)
print('add multi values: ', total)

### Sum list elements using a for loop
lst = [1, 2, 3, 3, 4, 4, 4, 5]

def sum_list_for_loop(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

total = sum_list_for_loop(lst)
print('sum list for: ', total)

### Sum list elements using the list sum() function 