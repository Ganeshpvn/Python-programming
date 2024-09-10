def count_negatives(lst):
    return sum(1 for num in lst if num < 0)

# Test the function
my_list = [16,-18,27,-16,23,-21,19]
print("Number of negative numbers:", count_negatives(my_list))