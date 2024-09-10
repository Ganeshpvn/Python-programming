def count_characters():
    uppercase = 0
    lowercase = 0
    numbers = 0
    while True:
        char = input("Enter any character: ")
        if char == '*':
            break
        elif char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbers += 1
    print("Total count of lower case:", lowercase)
    print("Total count of upper case:", uppercase)
    print("Total count of numbers =", numbers)
count_characters()