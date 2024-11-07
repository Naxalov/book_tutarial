from book import Book

book = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997, 10.99, True)
price = book.get_price()
print(price)
book.apply_discount(20)
print(book.get_price())