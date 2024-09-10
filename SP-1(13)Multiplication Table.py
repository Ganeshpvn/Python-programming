def print_multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
num = int(input("Input a number: "))
print_multiplication_table(num)