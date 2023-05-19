
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book
from flask_app.models.favorite_model import Favorite





@app.route('/books')
def books_home():
    all_books = Book.get_all_books()
    print(all_books)
    return render_template('books.html', all_books=all_books)


@app.route('/book/new', methods=['POST'])
def create_book():
    new_book = Book.save(request.form)
    return redirect('/books')

@app.route('/book/<int:id>')
def book_show(id):
    book = Book.get_all_favs_by_book({'id': id})
    all_authors = Author.get_all_authors()
    return render_template('book_show.html', book=book, all_authors=all_authors)