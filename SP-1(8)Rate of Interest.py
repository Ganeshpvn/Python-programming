def calculate_future_value(pv, r, n):
    fv = pv * (1 + r) ** n
    return round(fv, 2)
amt = 10000
int_rate = 3.5 / 100  # convert percentage to decimal
years = 7
future_value = calculate_future_value(amt, int_rate, years)
print("Future Value:", future_value)