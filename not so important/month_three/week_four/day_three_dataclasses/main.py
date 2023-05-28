# # You need to create a program to manage a list of books in a library. Each book has a title, an author, a publication year, and an ISBN.
# You need to define a Book class using the dataclass module that contains attributes for these properties.
# You also need to implement a Library class that manages a list of books.
# The Library class should allow you to add and remove books from the library,
# search for books by title or author, and display the list of books currently in the library

from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    ISBN: str


class Library:
    books: List[Book]

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        pass
