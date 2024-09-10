def print_rectangle(symbol, rows, cols, hollow):
    for i in range(rows):
        for j in range(cols):
            if hollow:
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    print(symbol, end=' ')
                else:
                    print(' ', end=' ')
            else:
                print(symbol, end=' ')
        print()
symbol = input("Enter the symbol: ")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
choice = input("Enter your choice (H/F): ")
if choice.upper() == 'H':
    hollow = True
elif choice.upper() == 'F':
    hollow = False
else:
    print("Invalid choice. Printing full rectangle by default.")
    hollow = False
print_rectangle(symbol, rows, cols, hollow)