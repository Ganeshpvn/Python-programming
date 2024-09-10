def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
# Get the input string from the user
input_string = input("Enter a string: ")
# Count the vowels and print the result
print("Number of vowels =", count_vowels(input_string))