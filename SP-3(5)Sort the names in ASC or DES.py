def sort_names():
    names = input("Enter the names separated by space: ").split()
    order = input("Order (A/D): ").upper()
    if order == "A":
        names.sort()
        print("Sorted names in ascending order:")
    elif order == "D":
        names.sort(reverse=True)
        print("Sorted names in descending order:")
    else:
        print("Invalid order choice. Please choose A or D.")
    print(" ".join(names))
sort_names()