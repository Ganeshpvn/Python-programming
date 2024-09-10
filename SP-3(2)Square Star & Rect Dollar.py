def print_star_square(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end=" ")
        print()
def print_dollar_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("$", end=" ")
        print()
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Star Square Pattern:")
print_star_square(rows, cols)
print("\nDollar Rectangle Pattern:")
print_dollar_rectangle(rows, cols)