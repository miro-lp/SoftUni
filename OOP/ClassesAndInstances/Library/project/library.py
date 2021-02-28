from .user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: User):
        if user.user_id in [u.user_id for u in self.user_records]:
            return f"User with id = {user.user_id} already registered in the library"
        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return f"We could not find such user to remove!"
        self.user_records.remove(user)
        self.rented_books.pop(user.username)

    def change_username(self, user_id: int, new_username: str):
        if user_id not in [u.user_id for u in self.user_records]:
            return f"There is no user with id = {user_id}!"
        for u in self.user_records:
            if u.user_id == user_id and u.username == new_username:
                return f"Please check again the provided username - it should be different than the username used so far!"
            elif u.user_id == user_id:
                self.rented_books[new_username] = self.rented_books[u.username]
                self.rented_books.pop(u.username)
                u.username = new_username
                break
