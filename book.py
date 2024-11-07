class Book:
    def __init__(self, title, author, genre, publication_year, price, availability=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.price = price
        self.availability = availability