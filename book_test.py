from book import Book

book = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951, 9.99, False)
# Create tests check book attributes
def test_book_attributes():
    assert book.title == "The Catcher in the Rye"
    assert book.author == "J.D. Salinger"
    assert book.genre == "Fiction"
    assert book.publication_year == 1951
   
    assert book.availability == False