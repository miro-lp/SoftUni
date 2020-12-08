head = input()
article = input()
comments = []
while True:
    comment = input()
    if comment == "end of comments":
        break
    comments.append(comment)

print("<h1>")
print(f"    {head}")
print("</h1>")
print("<article>")
print(f"    {article}")
print("</article>")
for i in comments:
    print("<div>")
    print(f"    {i}")
    print("</div>")