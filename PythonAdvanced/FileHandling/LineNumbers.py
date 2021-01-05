with open("text.txt", "r") as f:
    lines = f.readlines()

hints = [".", ",", "-", "!", "?", "'"]

new_f = open("output.txt", "w")
for i in range(1, len(lines) + 1):
    letters = [l for l in lines[i - 1] if l not in hints and l != " " and l != "\n"]
    marks = [c for c in lines[i - 1] if c in hints]
    print(f"Line {i}: {lines[i - 1].strip()} ({len(letters)})({len(marks)})", file=new_f)
new_f.close()