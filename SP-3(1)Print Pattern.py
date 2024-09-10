def print_pattern(number, max_times):
    for i in range(1, max_times + 1):
        print((str(number) + ' ') * i)
    for i in range(max_times - 1, 0, -1):
        print((str(number) + ' ') * i)
number = int(input("Enter the number to be printed: "))
max_times = int(input("Max number of times printed: "))
print_pattern(number, max_times)