def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1
# Test cases
print(is_power_of_three(27))  # Output: True
print(is_power_of_three(0))  # Output: False