def is_harshad(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0
num = int(input("Enter number: "))
if is_harshad(num):
    print("Given number is Harshad number")
else:
    print("Given number is not Harshad number")