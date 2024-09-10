def calculate_tax(income):
    if income <= 150000:
        tax = 0
    elif 150001 <= income <= 300000:
        tax = (income - 150000) * 0.10
    elif 300001 <= income <= 500000:
        tax = (150000 * 0.05) + ((income - 300000) * 0.20)
    else:
        tax = (150000 * 0.05) + (200000 * 0.20) + ((income - 500000) * 0.30)
    return tax
income = float(input("Enter the income: "))
tax = calculate_tax(income)
print("Tax: ", tax)