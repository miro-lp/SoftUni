books = input().split("&")

line = input()

while line != "Done":
    command = line.split(" | ")[0]
    book = line.split(" | ")[1]
    if command == "Add Book":
        if book not in books:
            books.insert(0, book)
    elif command == "Take Book":
        if book in books:
            books.remove(book)
    elif command == "Swap Books":
        book_2 = line.split(" | ")[2]
        if book and book_2 in books:
            index_1 = books.index(book)
            index_2 = books.index(book_2)
            books[index_1], books[index_2] = books[index_2], books[index_1]
    elif command == "Insert Book":
        books.append(book)
    elif command == "Check Book":
        index = int(book)
        if 0 <= index < len(books):
            print(books[index])

    line = input()

print(", ".join(books))