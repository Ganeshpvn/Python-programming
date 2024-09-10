import itertools

def find_combinations(num):
    # Convert the number to a string to easily extract digits
    num_str = str(num)
    
    # Use itertools.permutations to find all combinations
    combinations = itertools.permutations(num_str)
    
    # Print each combination
    for combination in combinations:
        print(''.join(combination))

# Test the function
num = int(input("Enter a 3-digit number: "))
find_combinations(num)
