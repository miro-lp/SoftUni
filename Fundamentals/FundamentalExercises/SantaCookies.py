batches = int(input())
total_boxes = 0
for i in range(batches):
    flour_in_grams = int(input())
    sugar_in_grams = int(input())
    cocoa_in_grams = int(input())
    flour_cups = flour_in_grams // 140
    sugar_spoon = sugar_in_grams // 20
    cacao_spoon = cocoa_in_grams // 10
    min_list = [flour_cups, sugar_spoon, cacao_spoon]
    total_cookes = (170) * min(min_list) // 25
    boxes = total_cookes // 5
    total_boxes += boxes
    if flour_cups < 1 or cacao_spoon < 1 or cacao_spoon < 1:
        print("Ingredients are not enough for a box of cookies.")
    else:
        print(f"Boxes of cookies: {boxes}")
print(f"Total boxes: {total_boxes}")
