import re

mails = []
while True:
    line = input()
    if not line:
        break
    pattern = r"w{3}.[A-Z a-z  \. 0-9\-]+\.[a-z]{2,}"
    matches = re.findall(pattern, line)
    if len(matches) == 1:
        mails.append(matches[0])

for i in mails:
    print(i)
