from collections import deque

customers = deque(map(int, input().split(", ")))
taxis = list(map(int, input().split(", ")))

total_time = 0
while len(customers) > 0 and len(taxis) > 0:
    if customers[0] <= taxis[-1]:
        total_time += customers.popleft()
        taxis.pop()
    elif customers[0] > taxis[-1]:
        taxis.pop()
if len(customers)==0:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
elif len(customers)>0:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str,customers))}")