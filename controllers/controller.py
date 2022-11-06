from flask import render_template, request, redirect

from app import app
from models.book import Book
from models.book_database import books_in_library, add_new_book, remove_book

@app.route('/books')
def index():
    print(books_in_library)
    return render_template('index.html', title='Books', all_books=books_in_library)

@app.route('/books/<index>')
def book_details(index):
    chosen_book = books_in_library[int(index)]
    return render_template('show.html', title='Book details', book=chosen_book)

@app.route('/books', methods=["POST"])
def adding_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title=title, author=author, genre=genre)
    add_new_book(new_book)
    return redirect('/books')

@app.route('/delete/<title>', methods=["POST"])
def deleting_item_from_library(title):
    remove_book(title)
    return redirect('/books')