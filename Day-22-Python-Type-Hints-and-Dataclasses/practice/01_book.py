from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    price: float


books = [
    Book("Python Crash Course", "Eric Matthes", 599.0),
    Book("Clean Code", "Robert C. Martin", 850.0),
    Book("Automate the Boring Stuff", "Al Sweigart", 499.5),
]

for book in books:
    print(book)
