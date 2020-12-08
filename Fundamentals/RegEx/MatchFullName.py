import  re

text = input()

search = r"(\b[A-Z][a-z]+\s[A-Z][a-z]+\b)"
matches = re.findall(search,text)


print(" ".join(matches))