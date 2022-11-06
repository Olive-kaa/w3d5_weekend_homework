from models.book import Book

book_1 = Book("The Man Who Died Twice", "Richard Osman", "crime fiction")
book_2 = Book("The Accidental Alchemist", "Gigi Pandian", "fantasy")
book_3 = Book("A Darker Shade of Magic", "V.E. Shwab", "fantasy")

books_in_library = [book_1, book_2, book_3]

def add_new_book(book):
    books_in_library.append(book)   #to be used in "new/ updated" page with new

def remove_book(book_title):
    book_to_remove = None
    for book in books_in_library:
        if book.title == book_title:
            book_to_remove = book
            break
        books_in_library.remove(book_to_remove)