def is_palindrome(s):
    #remove spaces and convert to lowercase
    s=s.replace("","").lower()
    #compare the string with its reverse
    return s==s[::-1]
#Test the function
print(is_palindrome("A man a plan a canal panama"))
#True
print(is_palindrome("Hello"))
#false