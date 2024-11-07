class Book:
    def __init__(self, title: str, author: str, genre: str, publication_year: int, price: float, availability: bool=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.price = price
        self.availability = availability

# Create an instance of the Book class
book = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997, 10.99, True)

# Accessing attributes
print(book.title)  # Output: Harry Potter and the Philosopher's Stone
print(book.author)  # Output: J.K. Rowling
print(book.genre)   # Output: Fantasy
print(book.publication_year)  # Output: 1997
print(book.price)  # Output: 10.99
print(book.availability)  # Output: True