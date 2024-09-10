def count_digits_and_numbers(s):
    digit_count = 0
    number_count = 0

    for char in s:
        if char.isdigit():
            digit_count += 1
            if char != '0' or (char == '0' and digit_count > 1):
                number_count += 1

    return digit_count, number_count

s = input("Enter a string: ")
digit_count, number_count = count_digits_and_numbers(s)

print("Number of digits:", digit_count)
print("Number of numbers:", number_count)
