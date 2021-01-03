def palindrome(word, index):
    if len(word) == 0:
        return True
    elif len(word) == 1:
        return True
    if word[0] == word[-1] and palindrome(word[1:-1], index):
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))