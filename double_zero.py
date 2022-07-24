# Завдання 2
def double_zero(array):
    result = []
    for digit in array:
        if digit == 0:
            result.extend([digit, digit])
        else:
            result.append(digit)
    return result


print(double_zero([1, 0, 2, 3, 0, 4, 5, 0]))
print(double_zero([1, 2, 3]))
