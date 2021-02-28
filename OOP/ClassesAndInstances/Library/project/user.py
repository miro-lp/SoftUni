from .library import Library


class User:
    books = []

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        if book_name in library.books_available[author]:
            if book_name in library.rented_books[self.username]:
                return f"The book \"{book_name}\" is already rented and will be available in {library.rented_books[self.username][book_name]} days!"
            library.rented_books[self.username][book_name] = days_to_return
            library.books_available[author].remove(book_name)
            User.books.append(book_name)

    def return_book(self, author: str, book_name: str, library: Library):
        if book_name not in User.books:
            return f"{self.username} doesn't have this book in his/her records!"
        library.rented_books[self.username].pop(book_name)
        library.books_available[author].append(book_name)
        User.books.remove(book_name)

    def info(self):
        return ", ".join(sorted(User.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {User.books}"
