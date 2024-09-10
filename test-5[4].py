def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    pattern_to_word = {}
    word_to_pattern = {}
    for p, w in zip(pattern, words):
        if p not in pattern_to_word and w not in word_to_pattern:
            pattern_to_word[p] = w
            word_to_pattern[w] = p
        elif pattern_to_word.get(p) != w or word_to_pattern.get(w) != p:
            return False
    return True
# Test cases
print(word_pattern("abba", "dog cat cat dog"))  # Output: True
print(word_pattern("abba", "dog cat cat fish"))  # Output: False