def count_special_characters(statement):
    special_characters = "!@#$%^&*()_-+={}:;<>?,./"
    count = 0
    for char in statement:
        if char in special_characters:
            count += 1
    return count
statement = input("Enter a statement: ")
print("Number of special characters:", count_special_characters(statement))