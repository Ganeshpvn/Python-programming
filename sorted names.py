def sort_names(names, order):
    if order.upper() == 'A':
        return sorted(names)
    elif order.upper() == 'D':
        return sorted(names, reverse=True)
    else:
        return "Invalid order choice. Please enter A for ascending or D for descending."
# Get the list of names from the user
names = input("Enter names separated by space: ").split()
# Get the order choice from the user
order = input("Order (A/D): ")
# Sort the names and print the result
print(sort_names(names, order))