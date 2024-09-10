def count_negative_numbers(numbers):
    count = 0
    for num in numbers:
        if num < 0:
            count += 1
    return count

numbers = [16, -18, 27, -16, 23, -21, 19]
print("List of elements =", numbers)
print("Number of negative numbers in List of elements =", count_negative_numbers(numbers))

