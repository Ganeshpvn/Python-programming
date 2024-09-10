def calculate_amount(purchasing_flat):
    base_price = 500
    if purchasing_flat > 2000:
        amount = purchasing_flat * base_price
    else:
        amount = 0  # or any other default value
    return amount

# Test the function
purchasing_flat = int(input("Enter the number of flats: "))
amount = calculate_amount(purchasing_flat)
print("The amount is: ₹", amount)
