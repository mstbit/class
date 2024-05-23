def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1))  # outputs: [1]
print(add_to(2))  # outputs: [1, 2]
print(add_to(3))  # outputs: [1, 2, 3]


### fix: use shallow copying
import copy
def add_to_2(num, target = []):
    if target:
        target = copy.copy(target)
    else:
        target = []
    target.append(num)
    return target

# print(add_to_2(1))  # outputs: [1]
# print(add_to_2(2))  # outputs: [2]
# print(add_to_2(3))  # outputs: [3]


def append_to(num, target=[]):
    target.append(num)
    return target

original_list = [1, 2, 3]
new_list = append_to(4, original_list)

print(original_list)  # Outputs:




def add_to_3(num, target=None):
    if target is None:
        target = []
    target.append(num)
    return target

print(add_to_3(1))  # outputs: [1]
print(add_to_3(2))  # outputs: [2]
print(add_to_3(3))  # outputs: [3]


