# class StringFunctions:
#     def __init__(self) -> None:
#         pass

#     @classmethod
#     def reverse_string(cls, text: str) -> str:
#         pass

from typing import List, Dict


class Book:
    def __init__(self, name: str, author: str, year: int, quantity: int) -> None:
        self.name = name
        self.author = author
        self.year = year
        self.quantity = quantity


class User:
    def __init__(self, name: str, surname: str, username: str) -> None:
        self.name = name
        self.surname = surname
        self.username = username


class Library:
    available_books: List[Book] = []
    registered_users: List[User] = []
    borrowed_books: Dict[str, Book] = {}

    @classmethod
    def add_books(cls, book: Book) -> None:
        cls.available_books.append(book)

    @classmethod
    def register_user(cls, user: User) -> None:
        cls.registered_users.append(user)

    @classmethod
    def show_how_many_copies_left(cls, book_name: str) -> None:
        for book in cls.available_books:
            if book_name == book.name and book.quantity != 0:
                print(f" there is {book.quantity} copies of '{book_name}' left")
                return
            else:
                print("There are no such books left")
                return

    @classmethod
    def borrow_book(cls, book_name: str, username: str) -> None:
        for book in cls.available_books:
            if book.name == book_name and book.quantity == 0:
                print("There are no copies left of this book")
                return
            else:
                book.quantity = book.quantity - 1
                cls.borrowed_books[username] = book
                return

    @classmethod
    def show_users(cls) -> None:
        for user in cls.registered_users:
            print(f"{user.name} {user.surname}, username: '{user.username}'")
        return

    @classmethod
    def show_books(cls) -> None:
        for book in cls.available_books:
            print(
                f"'books title: {book.name}', author: '{book.author}', published in {book.year}, copies left - {book.quantity}"
            )
        return

    @classmethod
    def show_borrowed_books(cls) -> None:
        for key, value in cls.borrowed_books.items():
            print(f"{key} borrowed '{value.name}'")


user_one = User(name="Antanas", surname="Fontanas", username="Fontanas123")
user_two = User(name="Rycka", surname="Nezinosi", username="Rycka123")


book_one = Book(
    name="The way of the superior man", author="David Deida", year=1997, quantity=10
)
book_two = Book(
    name="The 48 laws of power", author="Robert Greene", year=1998, quantity=8
)

Library.add_books(book_one)
Library.add_books(book_two)
Library.register_user(user_one)
Library.register_user(user_two)
Library.show_how_many_copies_left(book_name="The way of the superior man")
Library.borrow_book(book_name="The way of the superior man", username="Fontanas123")
Library.show_how_many_copies_left(book_name="The way of the superior man")
Library.show_users()
Library.show_books()
Library.show_borrowed_books()
