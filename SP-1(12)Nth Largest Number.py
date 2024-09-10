def nth_largest(numbers, n):
    if n < 1:
        return "Invalid input: N should be a positive integer"
    numbers = sorted(numbers, reverse=True)
    if n > len(numbers):
        return "Invalid input: N is larger than the list length"
    return numbers[n-1]
numbers = [14, 67, 48, 23, 5, 62]
n = int(input("Enter the value of N: "))
result = nth_largest(numbers, n)
if isinstance(result, str):
    print(result)
else:
    print(f"{n}th Largest number: {result}")
    