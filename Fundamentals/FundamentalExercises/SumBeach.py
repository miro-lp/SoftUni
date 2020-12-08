text = input().lower()

counter = 0

if "fish" in text:
    counter += text.count("fish")
if "sand" in text:
    counter += text.count("sand")
if "water" in text:
    counter += text.count("water")
if "sun" in text:
    counter += text.count("sun")

print(counter)
