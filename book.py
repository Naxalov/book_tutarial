class Book:
    def __init__(self, title: str, author: str, genre: str, publication_year: int, price: float, availability: bool=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.__price = price
        self.availability = availability

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
    
    def apply_discount(self, discount: float):
        self.__price = self.__price * (1 - discount/100)

