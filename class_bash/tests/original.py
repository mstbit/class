def append_to(num, target=[]):
    target.append(num)
    return target

original_list = [1, 2, 3]
new_list = append_to(4, original_list)

print(original_list)  # Outputs: [1, 2, 3, 4]
