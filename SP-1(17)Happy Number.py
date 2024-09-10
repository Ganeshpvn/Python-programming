def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1
num = int(input("Enter number: "))
if is_happy(num):
    print("Given number is happy number")
else:
    print("Given number is not happy number")