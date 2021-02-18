def stock_availability(boxes, *args):
    command = args[0]
    if command == "delivery":
        for item in args[1:]:
            boxes.append(item)
    elif command == "sell":
        if len(args) == 1:
            boxes = boxes[1:]
        elif len(args) == 2 and str(args[-1]).isdigit():
            if len(boxes) <= args[-1]:
                boxes = []
            else:
                boxes = boxes[args[-1]:]
        else:
            for item in args[1:]:
                if item in boxes:
                    while item in boxes:
                        boxes.remove(item)
    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
