def remove_duplicates(arr):
    return list(set(arr))
arr = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("Original array:", arr)
print("Array without duplicates:", remove_duplicates(arr))