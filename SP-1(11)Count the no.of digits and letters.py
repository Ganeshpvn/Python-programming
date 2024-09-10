def count_digits_letters(s):
    digits = sum(c.isdigit() for c in s)
    letters = sum(c.isalpha() for c in s)
    return letters, digits
s = input("Enter a string: ")
letters, digits = count_digits_letters(s)
print(f"Letters: {letters}")
print(f"Digits: {digits}")