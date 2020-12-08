from re import finditer

pattern = r"(^|(?<=\s))(([A-Z|a-z|0-9]+)([\.|_|\-][A-Z|a-z|0-9|]+)*@[A-Z|a-z|0-9]+([\.|-][a-z]+)*\.[a-z]+)\b"
matches = finditer(pattern,input())

print(*[i.group()for i in matches],sep="\n")