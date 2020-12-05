companies_id = {}

while True:
    command = input()
    if command == "End":
        break
    token = command.split(" -> ")
    if token[0] not in companies_id:
        companies_id[token[0]] = []
    if token[1] not in companies_id[token[0]]:
        companies_id[token[0]].append(token[1])

companies_id = dict(sorted(companies_id.items(), key= lambda x: x[0]))

for i in companies_id:
    print(f"{i}")
    for i in companies_id[i]:
        print(f"-- {i}")
