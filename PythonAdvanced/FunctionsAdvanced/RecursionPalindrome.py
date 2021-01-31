def palindrome(word, index):
    if len(word)-index*2 == 0 or len(word)-index*2 == 1:
        return f"{word} is a palindrome"
    if word[index] == word[len(word)-1-index]:
        return palindrome(word, index+1)
    else:
        return (f"{word} is not a palindrome")


print(palindrome("abcba", 0))
print(palindrome("abccba", 0))
print(palindrome("abcrba", 0))
print(palindrome("abcbar", 0))