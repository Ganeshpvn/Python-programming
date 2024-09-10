def is_tech_number(s):
    return s.isdigit() and len(s) == 10

s = input("Enter a string: ")
if is_tech_number(s):
    print(s, "is a tech number")
else:
    print(s, "is not a tech number")