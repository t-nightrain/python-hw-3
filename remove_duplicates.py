# Завдання 3
def remove_duplicates(array):
    result = []
    [result.append(digit) for digit in array if digit not in result]
    return result


# Варіант 2
# def remove_duplicates(array):
#     return list(dict.fromkeys(array))


print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1]))
