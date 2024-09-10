def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(num))
        temp //= 10
    return sum == num
num = int(input("Enter number: "))
if is_armstrong(num):
    print("Given number is Armstrong number")
else:
    print("Given number is not Armstrong number")