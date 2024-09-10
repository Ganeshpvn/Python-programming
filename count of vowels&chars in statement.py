def count_vowels_consonants(statement):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in statement:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
statement = input("Enter a statement: ")
count_vowels_consonants(statement)