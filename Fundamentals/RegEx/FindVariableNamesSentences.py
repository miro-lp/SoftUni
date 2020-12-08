import re

text = input()

pattern = r"\b_([A-Z|a-z|0-9]+)\b"

matches = re.findall(pattern,text)

print(",".join(matches))