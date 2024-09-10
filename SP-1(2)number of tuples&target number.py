def count_target_number(numbers, target):
    count = numbers.count(target)
    print("Count of", target, "in the tuple:", count)
# Get the tuple of numbers and target number from the user
numbers =tuple(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target number: "))
# Call the function to count the occurrences of the target number
count_target_number(numbers, target)