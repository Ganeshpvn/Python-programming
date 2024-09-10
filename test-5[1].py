def count_bits(n):
    ans = []
    for i in range(n + 1):
        ans.append(bin(i).count('1'))
    return ans

# Test cases
print(count_bits(2))  # Output: [0, 1, 1]
print(count_bits(5))  # Output: [0, 1, 1, 2, 1, 2]