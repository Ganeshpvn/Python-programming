def print_numbers(P, Q, R):
    for num in range(P, Q+1):
        if str(R) not in str(num):
            print(num, end=", ")
P = 60
Q = 70
R = 3
print("Numbers are = ", end="")
print_numbers(P, Q, R)