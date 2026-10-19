"""Lesson 5: classes and dataclasses."""
from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    author: str
    tags: list = field(default_factory=list)

    def matches(self, query: str) -> bool:
        query = query.lower()
        return query in self.title.lower() or query in self.author.lower()


class Library:
    def __init__(self):
        self._books = []

    def add(self, book: Book) -> None:
        self._books.append(book)

    def search(self, query: str):
        return [book for book in self._books if book.matches(query)]

    def __len__(self) -> int:
        return len(self._books)


def lesson() -> list:
    library = Library()
    library.add(Book("Dune", "Frank Herbert", ["scifi"]))
    library.add(Book("Deep Work", "Cal Newport"))
    return [len(library), [b.title for b in library.search("deep")]]
